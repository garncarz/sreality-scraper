from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import ClauseElement

from .database import Base, db_session


# https://gist.github.com/codeb2cc/3302754
def get_or_create(_model, _session=db_session, _defaults={}, **kwargs):
    query = _session.query(_model).filter_by(**kwargs)

    instance = query.first()

    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items()
                      if not isinstance(v, ClauseElement))
        params.update(_defaults)
        instance = _model(**params)

        db_session.add(instance)
        return instance, True


class Ad(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    image = Column(String)
    hash_id = Column(String, index=True, unique=True)
