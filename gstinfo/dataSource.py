import sqlalchemy
from sqlalchemy import *
import sqlalchemy.dialects.mysql.pymysql

#engine = create_engine('mysql+pymysql://username:password@dbserverIP/dbname')
engine = create_engine('mysql+pymysql://root:root@localhost/gst')
metadata = MetaData()
connection = engine.connect()

connectionInfo = dict(engine=engine, metadata=metadata, connection=connection)

def getConnectionInfo():
    return connectionInfo

taxinfo = Table('taxinfo', metadata, schema = 'gst', autoload = True, autoload_with = engine)

print('\nTo get the description of the table \n',repr(taxinfo))