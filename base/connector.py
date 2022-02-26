

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta


def create_session(user: str, password: str, dbname: str, host: str, port: int):
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
    session = sessionmaker(bind=engine)()

    return session


def create_table(dec_base: DeclarativeMeta, user: str, password: str, dbname: str, host: str, port: int):
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
    dec_base.metadata.create_all(engine)
