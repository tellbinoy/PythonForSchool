from gstinfo import dataSource
from sqlalchemy import Table,insert, select
import sqlalchemy.dialects.mysql.pymysql
import pandas as pd

connectionInfo = dataSource.getConnectionInfo()

taxinfo = Table('taxinfo', connectionInfo['metadata'], schema = 'gst', autoload = True, autoload_with = connectionInfo['engine'])

#This method just inserts one row in the table
def insertToTable(item, val=0, rate=0, type = 'none'):
    print('Insert started')
    #print(' item is ',item,' value ',val,' rate ',rate,' type ',type)
    try:
        stmt = insert(taxinfo).values(
        Item= item,
        Value = float(val),
        Taxrate = float(rate),
        Type = type,
        Price = (float(val)+( float(val) * ( float(rate) /100 )))
        )
        connectionInfo['engine'].execute(stmt)
        print('Insert successful')

    except Exception as e:
        print('Insert failed ',e)

#This method gives all the data in the table
def selectAllData():
    stmt = select([taxinfo])
    print(' Stmt for select is ',stmt)
    Resultset = connectionInfo['connection'].execute(stmt).fetchall()
    print('\nThe select Result is \n',Resultset)
    fullData = pd.DataFrame(Resultset)
    print('fullData ',fullData)
    return fullData


#This method selects by primary key - expect only one row to be returned if found
def selectItem(itemName):
    stmt = select([taxinfo]).where(taxinfo.c.Item == itemName)
    print(' Stmt for select is ',stmt)
    Resultset = connectionInfo['connection'].execute(stmt).fetchall()
    print('\nThe select Result is \n',Resultset)
    print('End - selectItem')
    return Resultset

#This method selects by non-primary key - expect one or more rows to be returned if found
def countItemByType(itemType):
    stmt = select([taxinfo]).where(taxinfo.c.Type == itemType)
    print(' Stmt for select is ', stmt)
    Resultset = connectionInfo['connection'].execute(stmt).fetchall()
    print('\nThe select Result is \n', Resultset)
    print('End - countItem')
    return Resultset


