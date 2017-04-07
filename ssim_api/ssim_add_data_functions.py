from ssim_api.ssim_general_functions import *
from ssim_api.ssim_query_functions import project_summary
#from ssim_api.ssim_build_table_functions import *
from ssim_api.all_dictionaries import table_name_dic, table_insert_dic
import pandas as pd
import sqlite3

def add_scenario_data(in_csv, sqlite_connection, data_type, index=None):
    # query database and build new tables for web application
    #
    # Args
    #   output_table: character string for name of new database, corresponds to a query name in all_dictionaries.py/query_dictionary
    #   sqlLiteConnection: connection to a SQLite database
    #
    # Returns:
    #   builds table specified
   # data_type = "stateclass"
    print("adding data to " + data_type + "table")
    output_table = table_name_dic[data_type]

    df = pd.read_csv(in_csv)

    summary_data = project_summary(sqlite_connection)
    #print(summary_data[0])
    #scenario_lookup = summary_data[0].set_index('Name').to_dict()
    strata_lookup = summary_data[5].set_index('Name').to_dict()
    secondary_strata_lookup = summary_data[6].set_index('Name').to_dict()
    state_labels_x_lookup = summary_data[1].set_index('Name').to_dict()
    state_labels_y_lookup = summary_data[2].set_index('Name').to_dict()
    stateclass_lookup = summary_data[7].set_index('Name').to_dict()
    transition_group_lookup = summary_data[3].set_index('Name').to_dict()
    stock_type_lookup = summary_data[8].set_index('Name').to_dict()

    if data_type=='stateclass':
        df = df.replace({"StratumID": strata_lookup["StratumID"]})
        df = df.replace({"SecondaryStratumID": secondary_strata_lookup["SecondaryStratumID"]})
        df = df.replace({"StateClassID": stateclass_lookup["StateClassID"]})
        df = df.replace({"StateLabelXID": state_labels_x_lookup["StateLabelXID"]})
        df = df.replace({"StateLabelYID": state_labels_y_lookup["StateLabelYID"]})
    if data_type=='transition':
        df = df.replace({"StratumID": strata_lookup["StratumID"]})
        df = df.replace({"SecondaryStratumID": secondary_strata_lookup["SecondaryStratumID"]})
        df = df.replace({"TransitionGroupID": transition_group_lookup["TransitionGroupID"]})

    if data_type == 'stock':
        df = df.replace({"StratumID": strata_lookup["StratumID"]})
        df = df.replace({"SecondaryStratumID": secondary_strata_lookup["SecondaryStratumID"]})
        df = df.replace({"StateClassID": stateclass_lookup["StateClassID"]})
        df = df.replace({"StockTypeID": stock_type_lookup["StockTypeID"]})

    write_frame(df, output_table, sqlite_connection)
    print("data added successfully")
    del df

    if index == True:
        index_table(data_type, sqlite_connection)
    print("done")

def read_db(sql, con):
    return pd.read_sql(sql, con)

def table_exists(name=None, con=None):
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='MYTABLE';".replace('MYTABLE', name)
    df = read_db(sql, con)
    #print(sql, df)
    print('table_exists?', len(df))
    exists = True if len(df)>0 else False
    return exists

def write_frame(frame, name, con):
    """
    Write records stored in a DataFrame to specified dbms.
    """
    with sqlite3.connect(con, detect_types=sqlite3.PARSE_DECLTYPES) as conn:

        insert_sql = table_insert_dic[name]

        if table_exists(name, conn):
            wildcards = ','.join(['?'] * len(frame.columns))

            insert_sql = insert_sql % (name, wildcards)
            frame.ScenarioID = frame.ScenarioID.astype(float)
            data = [tuple(x) for x in frame.values]
            conn.executemany(insert_sql, data)
            conn.commit()

def remove_scenario(sqlite_file, data_type, scenario):
    table = table_name_dic[data_type]
    sql = 'DELETE FROM %s WHERE ScenarioID = %s;' % (table, str(scenario))
    conn = sqlite3.connect(sqlite_file)
    conn.execute(sql)
    conn.commit()
    print("scenario %s removed from %s" % (str(scenario), table))

def index_exists(sqlite_file, table):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('PRAGMA INDEX_LIST({tn});'.format(tn=table))
    for row in c:
        return row

def index_table(data_type, sqlite_file):
    print("re-indexing table")
    table = table_name_dic[data_type]
    query_sql = 'SELECT * FROM {tn}'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute(query_sql.\
        format(tn=table))
    c.close()
    #result = c.fetchall()
    names = [description[0] for description in c.description]
    names.remove("Amount")
    names = tuple(names)

    index_name = table+"_Index"


    if index_exists(sqlite_file, table):
        print("delete index")
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('DROP INDEX {ix}'.format(ix=index_name))


    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('CREATE INDEX {ix} ON {tn}{cn}' \
              .format(ix=index_name, tn=table, cn=names))
    print("table indexed")
    conn.commit()
    conn.close()