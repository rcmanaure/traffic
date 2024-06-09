from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    """
    Verify the password against the hashed password

    :param plain_password: str
    :param hashed_password: str

    :return: bool
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    """
     Hash the password

    :param password: str

    :return: str (hashed password)
    """
    return pwd_context.hash(password)
