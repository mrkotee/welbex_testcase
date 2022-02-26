
import os

user = os.environ.get("SQL_USER", "user")
password = os.environ.get("SQL_PASSWORD", "password")
dbname = os.environ.get("SQL_DATABASE")
host = os.environ.get("SQL_HOST", "localhost")
port = os.environ.get("SQL_PORT", "5432")


# SECRET_KEY = os.environ.get("SECRET_KEY")
#
# DEBUG = int(os.environ.get("DEBUG", default=0))

