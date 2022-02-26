import os
from datetime import datetime as dt
import requests
import random
from sqlalchemy.orm import Session

from models import Base, Resource
from connector import create_table, create_session


def get_words(number: int):
    response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    words = response.text.splitlines()
    return words[:number]


def fill_base_with_random_data(session: Session):
    words = get_words(100)
    for word in words:
        random_date = dt.now().date().replace(day=random.randint(1, 28), month=random.randint(1, 12))
        session.add(
            Resource(date=random_date,
                     name=word,
                     amount=random.randint(1, 200),
                     distance=random.randint(1, 100)
                     )
        )
    session.commit()


if __name__ == '__main__':

    user = os.environ.get("SQL_USER", "user")
    password = os.environ.get("SQL_PASSWORD", "password")
    dbname = os.environ.get("SQL_DATABASE")
    host = os.environ.get("SQL_HOST", "localhost")
    port = os.environ.get("SQL_PORT", "5432")

    dbname = "psgr_dev"
    user = "psgr_user"
    password = "psgr_pswrd"

    create_table(Base, user, password, dbname, host, port)

    session = create_session(user, password, dbname, host, port)

    fill_base_with_random_data(session)
