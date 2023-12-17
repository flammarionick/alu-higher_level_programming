#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # MySQL server configurations
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    host, port = "localhost", 3306

    # Create the engine and bind it to the Base class
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@{host}:{port}/{database}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the first state
    first_state = session.query(State).order_by(State.id).first()

    # Check if the states table is empty
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    # Close the session
    session.close()
