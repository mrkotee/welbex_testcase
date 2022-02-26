import os
from datetime import datetime as dt
import requests
import random
from sqlalchemy.orm import Session

from base.models import Base, Resource
from base.connector import create_table, create_session


def get_words(number: int):
    """Get [number] words in alphabetical order"""
    response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    words = response.text.splitlines()
    return words[:number]


def fill_base_with_random_data(session: Session, size: int = 100) -> None:
    """

    :param session: sqlalchemy session
    :param size: number of record in DB to add
    """
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


def main():
    """Create Resource table in DB and fill it with random data"""
    from config import DBUSER, DBPASSWORD, DBNAME, HOST, PORT

    create_table(Base, DBUSER, DBPASSWORD, DBNAME, HOST, PORT)

    session = create_session(DBUSER, DBPASSWORD, DBNAME, HOST, PORT)

    resources = session.query(Resource).all()

    if not resources:
        fill_base_with_random_data(session)


if __name__ == '__main__':
    main()
