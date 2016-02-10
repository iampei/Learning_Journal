from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode, 
    UnicodeText,
    DateTime,
    )
import datetime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)


class Entry (Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique = True, nullable=False)
    body = Column(UnicodeText)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


    @classmethod
    def all (cls, session = None):
        if session is None:
            session = DBSession
        #return [(o.id, o.title, o.body, o.created, o.edited) for o in session.query(cls).order_by(cls.created.desc())]
        return session.query(cls).order_by(cls.created.desc())
    @classmethod
    def by_id (cls,id, session = None):
        if session is None:
            session = DBSession
        return session.query(cls).get(id)


#Index('my_index', MyModel.name, unique=True, mysql_length=255)