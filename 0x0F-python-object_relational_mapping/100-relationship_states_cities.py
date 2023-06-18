#!/usr/bin/python3

""" Script that creates the State “California” with the City “San Francisco”"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    """ Function that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    session.add(new_city)
    session.commit()
    session.close()
