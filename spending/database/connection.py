from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from spending.database import MODEL_LIST

Base = declarative_base()

SESSION = None

def get_connection():
    """ Creates a new database connection """
    global SESSION

    if not SESSION:
        """ If no session, then we will want to create one and make sure all of our
        tables exist before we try and use them """

        engine = create_engine('postgres://ross:ross@127.0.0.1/lcc_spending')
        for mdl in MODEL_LIST:
            mdl.metadata.create_all(engine)

        DBSession = sessionmaker(engine)
        SESSION = DBSession()

    return SESSION
