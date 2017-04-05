from ssim_api.ssim_general_functions import *
from ssim_api.ssim_query_functions import project_summary
from ssim_build_table_functions import *
import sys

def add_scenario(in_csv, output_table, sqlite_connection, scenario_id=None):
    # query database and build new tables for web application
    #
    # Args
    #   output_table: character string for name of new database, corresponds to a query name in all_dictionaries.py/query_dictionary
    #   sqlLiteConnection: connection to a SQLite database
    #
    # Returns:
    #   builds table specified

    df = pd.read_csv(r"F:\2016_Working\jts_2016_09_01_LandCarbon_CDI\ssim_api_external_update\stateclass.csv")

    #scenario_list = list(project_summary(sqlite_connection)[0]['scenario_id'])
    if scenario_id==None:
        scenario_list = list(project_summary(sqlite_connection)[0]["ScenarioID"])
        scenario_id = max(scenario_list) + 1

    summary_data = project_summary(sqlite_connection)
    strata_lookup = summary_data[5].set_index('Name').to_dict()
    secondary_strata_lookup = summary_data[6].set_index('Name').to_dict()
    state_labels_x_lookup = summary_data[1].set_index('Name').to_dict()
    stateclass_lookup = summary_data[7].set_index('Name').to_dict()

    #strata_lookup = dict([(str(k), v) for k, v in strata_lookup["StratumID"].items()])


    df = df.replace({"StratumID": strata_lookup["StratumID"]})

    df = df.replace({"SecondaryStratumID": secondary_strata_lookup["SecondaryStratumID"]})

    df = df.replace({"StateClassID": stateclass_lookup["StateClassID"]})
    df = df.replace({"StateLabelXID": state_labels_x_lookup["StateLabelXID"]})
    print(scenario_id)
    #df.insert(0, 'ScenarioID', scenario_id)

    df['ScenarioID'] = scenario_id
    print(df)
    operation = 'append'


    df_to_db(sqlite_connection, output_table, df, operation)

    del df

def remove_scenario(scenario):
    scenario

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