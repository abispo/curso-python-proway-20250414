from config import connection, Base
from models import *

if __name__ == "__main__":
    Base.metadata.create_all(connection)