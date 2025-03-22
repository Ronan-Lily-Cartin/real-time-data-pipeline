from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

THE_BASE = "postgresql://postgres:6167@localhost/traffic_data"

steam_engine = create_engine(THE_BASE)

Session = sessionmaker(bind=steam_engine)

try:
    session = Session()
    print("Connection Success")
    # session.execute('SELECT 1')
    # print("Test query successful")

except OperationalError as e:
    print("Error connecting to the database")
    

