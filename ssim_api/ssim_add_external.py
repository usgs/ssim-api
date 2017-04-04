from ssim_api.ssim_general_functions import *
from ssim_api.ssim_query_functions import project_summary

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


