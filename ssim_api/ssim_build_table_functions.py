#Adapted from https://gist.github.com/catawbasam/3164289

from datetime import datetime
import pandas as pd
import numpy as np

def read_db(sql, con):
    return pd.read_sql(sql, con)

def table_exists(name=None, con=None):
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='MYTABLE';".replace('MYTABLE', name)
    df = read_db(sql, con)
    #print(sql, df)
    print('table_exists?', len(df))
    exists = True if len(df)>0 else False
    return exists

def write_frame(frame, name=None, con=None, if_exists='append'):
    """
    Write records stored in a DataFrame to specified dbms.

    if_exists:
        'fail'    - create table will be attempted and fail
        'replace' - if table with 'name' exists, it will be deleted
        'append'  - assume table with correct schema exists and add data.  if no table or bad data, then fail.
            ??? if table doesn't exist, make it.
        if table already exists.  Add: if_exists=('replace','append','fail')
    """

    """if if_exists=='replace' and table_exists(name, con):
        cur = con.cursor()
        cur.execute("drop table "+name)
        cur.close()

    if if_exists in ('fail','replace') or ( if_exists=='append' and table_exists(name, con)==False ):
        #create table
        schema = get_schema(frame, name)
        print('schema\n', schema)
        cur = con.cursor()
        cur.execute(schema)
        cur.close()
        print('created table')"""


    #bulk insert
    wildcards = ','.join(['?'] * len(frame.columns))
    print(name)
    insert_sql = 'INSERT INTO %s VALUES (%s)' % (name, wildcards)
    #print 'insert_sql', insert_sql
    data = [tuple(x) for x in frame.values]
    #print('data', data)
    #print(wildcards)
    cur = con.cursor()
    cur.executemany(insert_sql, data)
    con.commit()
    cur.close()
    return

def db_colname(pandas_colname):
    '''convert pandas column name to a DBMS column name
        TODO: deal with name length restrictions, esp for Oracle
    '''
    colname =  pandas_colname.replace(' ','_').strip()
    return colname

def get_schema(frame, name):
    #types = {'DATE':'TIMESTAMP', 'DATETIME':'TIMESTAMP', 'INT':'NUMBER','FLOAT':'NUMBER', 'VARCHAR':'VARCHAR2'} #deal with datatype differences
    types = {'DATE': 'TIMESTAMP', 'DATETIME': 'TIMESTAMP', 'INT': 'INTEGER', 'FLOAT': 'DOUBLE', 'VARCHAR': 'TEXT'}
    column_types = []
    dtypes = frame.dtypes
    for i,k in enumerate(dtypes.index):
        dt = dtypes[k]
        #print 'dtype', dt, dt.itemsize
        if str(dt.type)=="<type 'numpy.datetime64'>":
            sqltype = types['DATETIME']
        elif issubclass(dt.type, np.datetime64):
            sqltype = types['DATETIME']
        elif issubclass(dt.type, (np.integer, np.bool_)):
            sqltype = types['INT']
        elif issubclass(dt.type, np.floating):
            sqltype = types['FLOAT']
        else:
            sampl = frame[ frame.columns[i] ][0]
            #print 'other', type(sampl)
            if str(type(sampl))=="<type 'datetime.datetime'>":
                sqltype = types['DATETIME']
            elif str(type(sampl))=="<type 'datetime.date'>":
                sqltype = types['DATE']
            else:
                sqltype = types['VARCHAR']
        colname =  db_colname(k)  #k.upper().replace(' ','_')
        column_types.append((colname, sqltype))
    columns = ',\n  '.join('%s %s' % x for x in column_types)
    template_create = """CREATE TABLE %(name)s (
                      %(columns)s
                    );"""
    #print 'COLUMNS:\n', columns
    create = template_create % {'name' : name, 'columns' : columns}
    return create


def df_to_db(database, name, df, operation):
    #print('\nsqlite, using detect_types=sqlite3.PARSE_DECLTYPES for datetimes')
    import sqlite3
    with sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        #conn.row_factory = sqlite3.Row
        write_frame(df, name, con=conn, if_exists=operation)
        #df_sqlite = read_db('select * from '+name, con=conn)
        #print('loaded dataframe from sqlite', len(df_sqlite))
    print('done with sqlite')


