import os

try:
    from dotenv import find_dotenv, load_dotenv

    load_dotenv(find_dotenv())

except ModuleNotFoundError:
    pass


# Por algum motivo começou a quebrar e não consegui ajeitar a tempo :(

# SECRET_KEY = os.getenv("SECRET_KEY")
# ALGORITHM = os.getenv("ALGORITHM")
# ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
# DATABASE_CREDENTIALS = {
#     "user": os.getenv("USER"),
#     "password": os.getenv("PASSWORD"),
#     "host": os.getenv("HOST"),
#     "port": os.getenv("PORT"),
#     "database": os.getenv("DATABASE"),
# }

SECRET_KEY = "5e2e4e40d02e7fa607f41d852f9a0535d6db28e2568f61c3256230b5e004c12d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DATABASE_CREDENTIALS = {
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5433,
    "database": "postgres",
}
