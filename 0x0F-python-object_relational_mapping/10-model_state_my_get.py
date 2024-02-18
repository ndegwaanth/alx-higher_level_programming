#!/usr/bin/python3
"""
    script that prints the State object with
    the name passed as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name == '__main__':
    if sys.argv != 5:
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    conn = session.querry(State).filter(state.name == sys.argv[4]).first()

    if conn:
        print(State.id)
    else:
        print("Not found")
