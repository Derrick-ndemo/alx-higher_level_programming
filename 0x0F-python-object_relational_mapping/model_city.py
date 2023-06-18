#!/usr/bin/python3

""" Module that contains the City class """

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ City class inherits from Base class """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id', ondelete='CASCADE'),
                      nullable=False)
    state = relationship('State', backref='cities')
