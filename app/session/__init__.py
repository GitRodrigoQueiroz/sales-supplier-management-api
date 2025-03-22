import os

try:
    from dotenv import find_dotenv, load_dotenv

    load_dotenv(find_dotenv())

except ModuleNotFoundError:
    pass

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
DATABASE_CREDENTIALS = {
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "host": os.getenv("HOST"),
    "port": os.getenv("PORT"),
    "database": os.getenv("DATABASE"),
}
