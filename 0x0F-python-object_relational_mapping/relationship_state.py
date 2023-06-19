#!/usr/bin/python3

""" State Module for HBNB project """

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(Base):
    """ State class """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete")
