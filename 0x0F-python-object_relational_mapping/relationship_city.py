#!/usr/bin/python3

""" Module that contains the class definition of a City and an instance
    Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """ Class that defines a City
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id, ondelete='CASCADE'), nullable=False)
    state = relationship('State', back_populates='cities')
