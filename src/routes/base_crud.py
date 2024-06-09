import logging
from uuid import UUID

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_sqlalchemy
from fastapi_filter.contrib.sqlalchemy import Filter


def raise_error_response(e: str) -> None:
    """
    Raise a HTTPException with a 409 status code  if the error is a duplicate\n
    entry, else raise a HTTPException with a 500 status code

    Args:
        e (str): The error message
    """

    status_code = 500
    detail = str(e)
    logging.error(f"Database: {detail}")
    if "duplicate key value violates unique constraint" in str(e):
        status_code = 409
        detail = "Duplicate entry"
    elif "ForeignKeyViolationError" in str(e):
        status_code = 409
        detail = "Foreign key violation. Key is not present in table."

    raise HTTPException(status_code=status_code, detail=detail)


class DatabaseCRUD:
    """
    A class to handle CRUD operations on a database

    Attributes:
        db_session (Session): The database session

    Methods:
        get_by_id(model, id: UUID) -> query: Get a row by id
        create_row(model, data: dict) -> model: Create a new row in the database
        update_row(model, id: UUID, data: BaseModel | dict) -> model: Update a row in the database
        delete_by_id(model, id: UUID) -> No content: Delete a row in the database
        get_all(model, limit: int = 100, offset: int = 0) -> query: Get all rows in the model table
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_by_id(self, model, id: UUID):
        """Get a row by id

        Args:
            model (sqlalchemy model): The model to query
            id (UUID): The id of the row to query

        Raises:
            HTTPException: If the row is not found

        Returns:
            query: The query result
        """
        with self.db_session as db:
            try:
                response = db.query(model).get(id)
            except SQLAlchemyError as e:
                db.rollback()
                logging.error(e)
                raise HTTPException(status_code=500, detail=str(e))
            else:
                return response

    def create_row(self, model, data: BaseModel):  # noqa
        """Create a new row in the database in the model table

        Args:
            model (sqlalchemy model): The model to use
            data (dict): The data to create the model with

        Raises:
            HTTPException: If the model generation fails

        Returns:
            model: The created model
        """
        with self.db_session as db:
            try:
                if not isinstance(data, dict):
                    data = data.model_dump(exclude_unset=True)
                if not data:
                    # Handle the case where no data is provided for update
                    raise ValueError("No data provided for update")
                model_instance = model(**data)
                db.add(model_instance)
                db.commit()
                db.refresh(model_instance)
            except SQLAlchemyError as e:
                db.rollback()
                raise_error_response(e)
            else:
                return model_instance

    def update_row(self, model, id: UUID, data: BaseModel | dict):
        """Update a row in the database in the model table  with the given data

        Args:
            model (sqlalchemy model): The model to update
            id (UUID): The id of the row to update
            data (BaseModel | dict): The data to update the row

        Raises:
            HTTPException: If the row is not found or the update fails

        Returns:
            model: The updated row
        """
        with self.db_session as db:
            try:
                if not isinstance(data, dict):
                    data = data.model_dump(exclude_unset=True)
                if not data:
                    # Handle the case where no data is provided for update
                    raise ValueError("No data provided for update")
                response = db.query(model).get(id)
                if not response:
                    return None
                db.query(model).filter(model.id == id).update(data)
                db.commit()
            except SQLAlchemyError as e:
                db.rollback()
                raise_error_response(e)
            else:
                db.refresh(response)
                return response

    def delete_by_id(self, model, id: UUID):
        """Delete a row in the database in the model table

        Args:
            model (sqlalchemy model): The model to delete
            id (UUID): The id of the row to delete

        Raises:
            HTTPException: If the row is not found or the delete fails

        Returns:
            No content: The model is deleted
        """
        with self.db_session as db:
            try:
                db.query(model).filter(model.id == id).delete()
                db.commit()
            except SQLAlchemyError as e:
                db.rollback()
                raise HTTPException(status_code=500, detail=str(e))
            else:
                return True

    def get_all(
        self,
        model,
        filters: Filter,
        join_models: list = None,
    ):
        """Get all rows in the model table

        Args:
            model (sqlalchemy model): The model to query
            filters (Filter): The filter object
            join_models (list): The models to join with the query model


        Returns:
            query: The query result
        """
        with self.db_session as db:
            try:
                query = select(model)

                if join_models:
                    for join_model in join_models:
                        query = query.join(join_model)

                query = filters.sort(query)
                query = filters.filter(query)

                query = paginate_sqlalchemy(db, query)
            except SQLAlchemyError as e:
                db.rollback()
                logging.error(e)
                raise HTTPException(status_code=500, detail=str(e))
            else:
                return query

    def get_by_field(self, model, field: str, value: str):
        """Get a row by field

        Args:
            model (sqlalchemy model): The model to query
            field (str): The field to query
            value (str): The value to query

        Raises:
            HTTPException: If the row is not found

        Returns:
            query: The query result
        """
        with self.db_session as db:
            try:
                response = (
                    db.query(model)
                    .filter(getattr(model, field) == value)
                    .first()
                )
            except SQLAlchemyError as e:
                db.rollback()
                logging.error(e)
                raise_error_response(e)
            else:
                return response
