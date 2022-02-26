

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import Session


def create_session(user: str, password: str, dbname: str, host: str, port: int) -> Session:
    """Create alchemy postgres session"""
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
    session = sessionmaker(bind=engine)()

    return session


def create_table(dec_base: DeclarativeMeta, user: str, password: str, dbname: str, host: str, port: int) -> None:
    """Create table of alchemy declarative base class"""
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
    dec_base.metadata.create_all(engine)
