#!/usr/bin/python3

""" Module that lists all State objects that contain the letter a from the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



if __name__ == "__main__":
    """ main function """

    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    # create a configured class Session
    Session = sessionmaker(bind=engine)

    # create a Session
    mySession = Session()

    # query to get all State objects that contain the letter a
    for state in mySession.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))

    # close session
    mySession.close()
