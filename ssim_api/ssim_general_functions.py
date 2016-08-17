# **********************************************************
# ssim_general_functions.py: helper functions and general
# query functions for querying .ssim output tables
# **********************************************************

# **********************************************************
# Setup
# **********************************************************
import sqlite3, sys, os.path
import pandas as pd
from ssim_api.all_dictionaries import query_dictionary

def apply_query(sqlite_connection, query_sql, all_params=None):
    # Creates connected to the database, executes query, and returns pandas dataframe with results
    #
    # Args:
    #   all_params: list of all parameters that will be queried with WHERE statement
    #   squery_sql: current sql statement
    #
    # Returns:
    #   sql statement with either WHERE or AND appended to the end
    #
    conn = sqlite3.connect(sqlite_connection)
    c = conn.cursor()
    if len(all_params) > 0:
        c.execute(query_sql, all_params)
    else:
        c.execute(query_sql)
    names = [description[0] for description in c.description]
    result = c.fetchall()
    df = pd.DataFrame(result, columns=names)
    return df

def table_exists(sqlite_connection, table):
    # checks to see if a aspecified table exists
    #
    # Args:
    #   sqlite_connection: path to sqLite db
    #   table: character string with name of table
    #
    # Returns:
    #   if exists returns a tuble with the table name
    #   if does not exits returns empty
    #
    query_sql = query_dictionary["TableExists"]
    conn = sqlite3.connect(sqlite_connection)
    c = conn.cursor()
    c.execute(query_sql, (table,))
    return c.fetchone()

def raise_type_error(value, variable_name=None):
    if variable_name:
        if type(value) != tuple:
            raise Exception("Value " + str(value) + " for " + variable_name + " is not a tuple. Must be of form (xxxx,) or (xxxx, xxxx)")
    else:
        if type(value) != tuple:
            raise Exception("Value " + str(value) + " is not a tuple. Must be of form (xxxx,) or (xxxx, xxxx)")

def raise_error_empty_df(df):
    if df.empty:
        raise Exception("Dataframe is empty. Check filtering parameters.")

def update_query_string(all_params, query_sql, query_column, variable, variable_name):
    # Appends WHERE or AND to Sql statement depending on whether parameter is the first parameter in the WHERE statement
    #
    # Args:
    #   all_params: list of all parameters that will be queried with WHERE statement
    #   squery_sql: current sql statement
    #
    # Returns:
    #   sql statement with either WHERE or AND appended to the end
    #
    raise_type_error(variable, variable_name=variable_name)
    if len(all_params) == 0:
        query_sql += " WHERE "
    else:
        query_sql += " AND "

    query_sql += query_column + " IN (" + ",".join("?" * len(variable)) + ")"
    all_params += variable

    return query_sql, all_params



# **********************************************************
# General database functions
# **********************************************************

def db_query_general(sqlite_connection, query_name, project_id=None, table_name_project=None, scenario_id=None, table_name_scenario=None):
    # General query function. Applies sql query on .ssim database
    #
    # Args:
    #   sqlLiteConnection: connection to a SQLite database
    #   query_name: name of query to apply stored in query_dictionary
    #   project_id: tuple with ProjectIDs for filtering query (optional - if not provided, all projects are included in results)
    #   table_name_project: table to filter by projectID (required if project_id is defined)
    #   scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)
    #   table_name_scenario: table to filter by ScenarioID (required if scenario_id is defined)
    #
    # Returns:
    #   A pandas dataframe with query results
    #
    query_sql = query_dictionary[query_name]
    all_params = ()
    if project_id:
        query_sql, all_params = update_query_string(all_params, query_sql, table_name_project + ".ProjectID", project_id,"project_id")
    if scenario_id:
        query_sql, all_params = update_query_string(all_params, query_sql, table_name_scenario + ".ScenarioID", scenario_id, "scenario_id")

    df = apply_query(sqlite_connection, query_sql, all_params)
    raise_error_empty_df(df)
    return df



