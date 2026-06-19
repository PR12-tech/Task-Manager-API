import os
from passlib.context import CryptContext # Password Hashing
from jose import jwt, JWTError #JWT Creation and Verification
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
# These above variables are used to sign JWT Tokens.


pwd_context = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
)
# Password Hashing Engine


def hash_password(password: str):
    return pwd_context.hash(password)
#Used during registration.


def verify_password(
        plain_password: str,
        hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
#Used during login and checks entered and stored(hashed) password.


def create_access_token(data: dict):

    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm = ALGORITHM
    )
# Creates JWT.


def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )

        username = payload.get("sub")

        return username

    except JWTError:

        return None
# Used when user access protected routes.