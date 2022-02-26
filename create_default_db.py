import os
from datetime import datetime as dt
import requests
import random
from sqlalchemy.orm import Session

from base.models import Base, Resource
from base.connector import create_table, create_session


def get_words(number: int):
    response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    words = response.text.splitlines()
    return words[:number]


def fill_base_with_random_data(session: Session, size: int = 100):
    words = get_words(size)
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
    from config import DBUSER, DBPASSWORD, DBNAME, HOST, PORT

    create_table(Base, DBUSER, DBPASSWORD, DBNAME, HOST, PORT)

    session = create_session(DBUSER, DBPASSWORD, DBNAME, HOST, PORT)

    resources = session.query(Resource).all()

    if not resources:
        fill_base_with_random_data(session)
