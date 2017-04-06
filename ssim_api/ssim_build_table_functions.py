#Adapted from https://gist.github.com/catawbasam/3164289


import pandas as pd


def read_db(sql, con):
    return pd.read_sql(sql, con)

def table_exists(name=None, con=None):
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='MYTABLE';".replace('MYTABLE', name)
    df = read_db(sql, con)
    #print(sql, df)
    print('table_exists?', len(df))
    exists = True if len(df)>0 else False
    return exists

def write_frame(frame, name=None, con=None):
    """
    Write records stored in a DataFrame to specified dbms.

    if_exists:
        'append'  - assume table with correct schema exists and add data.  if no table or bad data, then fail.
            ??? if table doesn't exist, make it.

    """

    if table_exists(name, con):
        wildcards = ','.join(['?'] * len(frame.columns))

        insert_sql = 'INSERT INTO %s (ScenarioID, Iteration, Timestep, StratumID, SecondaryStratumID, StateClassID, StateLabelXID, StateLabelYID, AgeMin, AgeMax, AgeClass, Amount) VALUES (%s)' % (name, wildcards)

        data = [tuple(x) for x in frame.values]

        con.executemany(insert_sql, data)
        con.commit()


def df_to_db(database, name, df):
    import sqlite3
    with sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        write_frame(df, name, con=conn)



