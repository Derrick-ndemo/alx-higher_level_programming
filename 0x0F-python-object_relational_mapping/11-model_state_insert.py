#!/usr/bin/python3

""" Script that adds the State object
    "Louisiana" to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """ Function that adds the State object "Louisiana" to the database
    hbtn_0e_6_usa
    """

    # Create engine that opens connection between the class state and
    # the database with the data of the user (passed by argument)
    user = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, database),
                           pool_pre_ping=True)

    # Makes a session for the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new state
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the new state id
    print(new_state.id)
    session.close()
