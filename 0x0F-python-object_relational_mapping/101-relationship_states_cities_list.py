#!/usr/bin/python3

""" Script that lists all State objects, and corresponding City objects, contained in the database hbtn_0c_101_usa"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ Engine creation """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    """ Session creation """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query """
    query = session.query(State).order_by(State.id).all()

    """ Print """
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
