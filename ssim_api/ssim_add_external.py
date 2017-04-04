from ssim_api.ssim_general_functions import *
from ssim_api.ssim_query_functions import project_summary
from ssim_build_table_functions import *

def add_scenario(in_csv, output_table, sqlite_connection):
    # query database and build new tables for web application
    #
    # Args
    #   output_table: character string for name of new database, corresponds to a query name in all_dictionaries.py/query_dictionary
    #   sqlLiteConnection: connection to a SQLite database
    #
    # Returns:
    #   builds table specified

    #scenario_list = list(project_summary(sqlite_connection)[0]['scenario_id'])
    df = pd.read_csv('../data/example.csv')

    operation = 'append'

    df_to_db(sqlite_connection, output_table, df, operation)

    del df


def index_exists(sqlite_file, table):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('PRAGMA INDEX_LIST({tn});'.format(tn=table))
    for row in c:
        return row

def index_table(table, sqlite_file):
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

    print(names)
    index_name = table+"_Index"
    print(index_name)

    if index_exists(sqlite_file, table):
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('DROP INDEX {ix}'.format(ix=index_name))
    else:
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('CREATE INDEX {ix} ON {tn}{cn}' \
                  .format(ix=index_name, tn=table, cn=names))

    conn.commit()
    conn.close()