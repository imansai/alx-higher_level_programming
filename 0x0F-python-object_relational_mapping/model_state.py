#!/usr/bin/python3
"""
Includes State class and Base as an instance of declarative_base().
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class with id and name attributes for every state.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
