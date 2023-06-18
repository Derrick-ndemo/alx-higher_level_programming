#!/usr/bin/python3

""" Script that lists all State objects from the database hbtn_0e_6_usa """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """ Function that lists all State objects from the database hbtn_0e_6_usa """

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    # dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, passwd, db), pool_pre_ping=True)

    # Generate database schema
    Base.metadata.create_all(engine)

    # SQLAlchemy ORM session factory bound to this engine
    Session = sessionmaker(bind=engine)

    # Create a new session
    session = Session()

    # Querying data
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
