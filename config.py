
import os

DBUSER = os.environ.get("SQL_USER", "user")
DBPASSWORD = os.environ.get("SQL_PASSWORD", "password")
DBNAME = os.environ.get("SQL_DATABASE")
HOST = os.environ.get("SQL_HOST", "localhost")
PORT = os.environ.get("SQL_PORT", "5432")

DEBUG = int(os.environ.get("DEBUG", default=0))
