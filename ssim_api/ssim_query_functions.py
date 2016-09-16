# **********************************************************
# ssim_query_functions.py: Functions for querying .ssim output tables
# **********************************************************

# **********************************************************
# Setup
# **********************************************************

import sqlite3, sys, os.path
import pandas as pd
from ssim_api.all_dictionaries import query_dictionary
from ssim_api.ssim_general_functions import *

# **********************************************************
# Query database functions
# **********************************************************

def db_query_stateclass(sqlite_connection, project_id=None, scenario_id=None, iteration=None, timestep=None, stratum=None, secondary_stratum=None, state_label_x=None, state_label_y=None):
    # Function for querying the STSim_OutputStratumState table in the database
    #
    # Args:
    #   sqlLiteConnection: connection to a SQLite database
    #   project_id: tuple with ProjectIDs for filtering query (optional - if not provided, all projects are included in results)
    #   scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)
    #   iteration: tuple with iteration values for filtering query (optional - if not provided, all iterations are included in results)
    #   timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results)
    #   stratum: tuple with strata values for filtering query (optional - if not provided, all strata are included in results)
    #   secondary_stratum: tuple with secondary strata values for filtering query (optional - if not provided, all secoondary strata are included in results)
    #   state_label_x: tuple with state label x values for filtering query (optional - if not provided, all state label x are included in results)
    #   state_label_y: tuple with state label y values for filtering query (optional - if not provided, all state label y are included in results)
    # Returns:
    #   Dataframe with the results of the query
    #
    try:
        query_name = "OutputStratumState_query"
        query_sql = query_dictionary[query_name]
        all_params = ()
        if project_id:
            query_sql, all_params = update_query_string(all_params, query_sql, "SSim_Scenario.ProjectID", project_id, "project_id")
        if scenario_id:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_OutputStratumState.ScenarioID", scenario_id, "scenario_id")
        if iteration:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_OutputStratumState.Iteration", iteration, "iteration")
        if timestep:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_OutputStratumState.Timestep", timestep, "timestep")
        if stratum:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_Stratum.Name", stratum, "stratum")
        if secondary_stratum:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_SecondaryStratum.Name", secondary_stratum, "secondary_stratum")
        if state_label_x:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_StateLabelX.Name", state_label_x, "state_label_x")
        if state_label_y:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_StateLabelY.Name", state_label_y, "state_label_y")

        df = apply_query(sqlite_connection, query_sql, all_params)
        raise_error_empty_df(df)
        return df

    except Exception as explanation:
        print("Error:", explanation)


def db_query_transitiongroup(sqlite_connection, project_id=None, scenario_id=None, iteration=None, timestep=None, stratum=None, secondary_stratum=None, transition_group=None):
    # Function for querying the STSim_OutputStratumState table in the database
    #
    # Args:
    #   sqlLiteConnection: connection to a SQLite database
    #   project_id: tuple with ProjectIDs for filtering query (optional - if not provided, all projects are included in results)
    #   scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)
    #   iteration: tuple with iteration values for filtering query (optional - if not provided, all iterations are included in results)
    #   timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results)
    #   stratum: tuple with strata values for filtering query (optional - if not provided, all strata are included in results)
    #   secondary_stratum: tuple with secondary strata values for filtering query (optional - if not provided, all secoondary strata are included in results)
    #   state_label_x: tuple with state label x values for filtering query (optional - if not provided, all state label x are included in results)
    #   state_label_y: tuple with state label y values for filtering query (optional - if not provided, all state label y are included in results)
    # Returns:
    #   Dataframe with the results of the query
    #
    try:
        query_name = "OutputStratumTransition_query"
        query_sql = query_dictionary[query_name]
        all_params = ()
        if project_id:
            query_sql, all_params = update_query_string(all_params, query_sql, "SSim_Scenario.ProjectID", project_id, "project_id")
        if scenario_id:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_OutputStratumTransition.ScenarioID", scenario_id, "scenario_id")
        if iteration:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_OutputStratumTransition.Iteration", iteration, "iteration")
        if timestep:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_OutputStratumTransition.Timestep", timestep, "timestep")
        if stratum:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_Stratum.Name", stratum, "stratum")
        if secondary_stratum:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_SecondaryStratum.Name", secondary_stratum, "secondary_stratum")
        if transition_group:
            query_sql, all_params = update_query_string(all_params, query_sql, "STSim_TransitionGroup.Name", transition_group, "transition_group")

        df = apply_query(sqlite_connection, query_sql, all_params)
        raise_error_empty_df(df)
        return df

    except Exception as explanation:
        print("Error:", explanation)

def db_query_stock(sqlite_connection, project_id=None, scenario_id=None, iteration=None, timestep=None, stratum=None, secondary_stratum=None, stateclass=None, stock_type=None):
    # Function for querying the STSim_OutputStratumState table in the database
    #
    # Args:
    #   sqlLiteConnection: connection to a SQLite database
    #   project_id: tuple with ProjectIDs for filtering query (optional - if not provided, all projects are included in results)
    #   scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)
    #   iteration: tuple with iteration values for filtering query (optional - if not provided, all iterations are included in results)
    #   timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results)
    #   stratum: tuple with strata values for filtering query (optional - if not provided, all strata are included in results)
    #   secondary_stratum: tuple with secondary strata values for filtering query (optional - if not provided, all secoondary strata are included in results)
    #   state_label_x: tuple with state label x values for filtering query (optional - if not provided, all state label x are included in results)
    #   state_label_y: tuple with state label y values for filtering query (optional - if not provided, all state label y are included in results)
    # Returns:
    #   Dataframe with the results of the query
    #
    query_name = "OutputStock_query"
    query_sql = query_dictionary[query_name]
    all_params = ()
    if project_id:
        query_sql, all_params = update_query_string(all_params, query_sql, "SSim_Scenario.ProjectID", project_id, "project_id")
    if scenario_id:
        query_sql, all_params = update_query_string(all_params, query_sql, "SF_OutputStock.ScenarioID", scenario_id, "scenario_id")
    if iteration:
        query_sql, all_params = update_query_string(all_params, query_sql, "SF_OutputStock.Iteration", iteration, "iteration")
    if timestep:
        query_sql, all_params = update_query_string(all_params, query_sql, "SF_OutputStock.Timestep", timestep, "timestep")
    if stratum:
        query_sql, all_params = update_query_string(all_params, query_sql, "STSim_Stratum.Name", stratum, "stratum")
    if secondary_stratum:
        query_sql, all_params = update_query_string(all_params, query_sql, "STSim_SecondaryStratum.Name", secondary_stratum, "secondary_stratum")
    if stateclass:
        query_sql, all_params = update_query_string(all_params, query_sql, "STSim_StateClass.Name", stateclass, "stateclass")
    if stock_type:
        query_sql, all_params = update_query_string(all_params, query_sql, "SF_StockType.Name", stock_type, "stock_type")

    df = apply_query(sqlite_connection, query_sql, all_params)
    raise_error_empty_df(df)
    return df

def query_output_options(sqlite_connection, scenario_id=None):
    # Function for quering STSim_OutputOptions table
    #
    # Args:
    #   sqlLiteConnection: connection to a SQLite database
    #   scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)
    #
    # Returns:
    #  Dataframe with output options table
    #
    #
    query_name = "OutputOptions"
    if scenario_id:
        df = db_query_general(sqlite_connection, query_name, project_id=None, table_name_project=None, scenario_id=scenario_id, table_name_scenario="STSim_OutputOptions")
    else:
        df = db_query_general(sqlite_connection, query_name, project_id=None, table_name_project=None, scenario_id=None, table_name_scenario=None)
    return df

def query_spatial_files_stateclass(sqlite_connection, scenario_id=None, iteration=None, timestep=None):
    # Function for quering spatial results
    #
    # Args:
    #   sqlLiteConnection: connection to a SQLite database
    #   scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)
    #   iteration: tuple with iteration values for filtering query (optional - if not provided, all iterations are included in results)
    #   timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results)
    # Returns:
    #  Dataframe with scenario_id, iteration, timestep, and path to spatial file
    #
    # Assumes db.ssim.output folder is in the same directory as the database
    #
    all_data = []
    db_name = os.path.basename(sqlite_connection)
    all_project_summary = project_summary(sqlite_connection)
    all_scenario_info = all_project_summary[0]

    if scenario_id == None:
        scenario_id = all_scenario_info.loc[all_scenario_info.RunStatus == 3, 'ScenarioID'].unique()

    for scenario in scenario_id:
        output_options = query_output_options(sqlite_connection, scenario_id=(int(scenario),))

        ##Check if spatial output is checked in STSim_OutputOptions table
        if output_options["RasterOutputAATP"][0] == -1:
            output_timestep = output_options["RasterOutputAATPTimesteps"][0]
            scenario_info = all_scenario_info.loc[all_scenario_info["ScenarioID"] == scenario].reset_index(drop=True)
            iterations_all = iteration
            if iteration == None:
                iteration_max = scenario_info["MaximumIteration"][0]
                iteration_min = scenario_info["MinimumIteration"][0]
                iterations_all = list(range(iteration_min, iteration_max + 1))

            if timestep == None:
                timestep_max = scenario_info["MaximumTimestep"][0]
                timestep_min = scenario_info["MinimumTimestep"][0]
                timestep = list(range(timestep_min, timestep_max + 1, output_timestep))

            for iter in iterations_all:
                for step in timestep:
                    iter = '{:0>4}'.format(iter)
                    step = '{:0>4}'.format(step)
                    file_path = os.path.join(db_name + ".output", "Scenario-" + str(
                        scenario), "Spatial", "It" + iter + "-Ts" + step + "-sc.tif")
                    spatial_info = [scenario, iter, step, file_path ]
                    all_data.append(spatial_info)


    columns = ["Scenario", "Iteration", "Timestep", "Path"]
    df = pd.DataFrame(all_data, columns=columns)

    return df

def query_spatial_files_tgap(sqlite_connection, scenario_id=None, timestep=None, transition_group=None):
    # Function for querying transition group average probability spatial files
    #
    # Args:
    #   sqlLiteConnection: connection to a SQLite database
    #   scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)
    #   timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results)
    #   transition_group: tuple with TransitionGroupIDs for filtering query (optional - if not provided, all timesteps are included in results)
    #
    # Returns:
    #   Dataframe with scenario_id, timestep, transitiongroupID and path to spatial file
    #
    # Assumes db.ssim.output folder is in the same directory as the database
    #
    all_data = []
    db_name = os.path.basename(sqlite_connection)
    all_project_summary = project_summary(sqlite_connection)
    all_scenario_info = all_project_summary[0]
    all_transition_group_info = all_project_summary[3]

    if scenario_id == None:
        ##Return scenario ids for scenarios that have been run
        scenario_id = all_scenario_info.loc[all_scenario_info.RunStatus == 3, 'ScenarioID'].unique()

    if transition_group == None:
        transition_group = list(all_transition_group_info["TransitionGroupID"])

    for scenario in scenario_id:

        output_options = query_output_options(sqlite_connection, scenario_id=(int(scenario),))

        ##Check if spatial output is checked in STSim_OutputOptions table
        if output_options["RasterOutputAATP"][0] == -1:
            output_timestep = output_options["RasterOutputAATPTimesteps"][0]

            scenario_info = all_scenario_info.loc[all_scenario_info["ScenarioID"] == scenario].reset_index(drop=True)

            if timestep == None:
                timestep_max = scenario_info["MaximumTimestep"][0]
                timestep_min = scenario_info["MinimumTimestep"][0]
                timestep = list(range(timestep_min, timestep_max + 1, output_timestep))
                timestep.pop(0)


            for step in timestep:
                step = '{:0>4}'.format(step)
                for transition in transition_group:
                    file_path = os.path.join(db_name + ".output", "Scenario-" + str(scenario), "Spatial", "It0000" + "-Ts" + step + "-tgap-" + str(transition) + ".tif")
                    all_data.append([scenario, step, transition, file_path ])

    columns = ["Scenario", "Timestep", "TransitionGroupID", "Path"]
    df = pd.DataFrame(all_data, columns=columns)

    return df

def query_projects(sqlite_connection):
    # function to get all project names and ids for a .ssim database
    #
    # Args:
    #   sqlite_connection: path to sqLite db
    #
    # Returns:
    #   A pandas dataframe with projectID and Name as headers
    #
    projects = db_query_general(sqlite_connection, 'Project_Ids', project_id=None, table_name_project=None, scenario_id=None, table_name_scenario=None)
    return projects

def project_summary(sqlite_connection, project=None):
    # creates a summary of parameters for from a project in a sqlite database
    #
    # Args:
    #   sqlite_connection: path to sqLite db
    #   project_id: tuple with ProjectIDs for filtering query (optional - if not provided, all projects are included in results)
    #
    # Returns:
    #   A list of pandas dataframes:
    #        ls[0] = scenarios(Names, IDs, and RunControl info)
    #        ls[1] = state_labels_x (StateLabelXID, Name, Description)
    #        ls[2] = state_labels_y (StateLabelYID, Name, Description)
    #        ls[3] = transition_groups (TransitionGroupID, Name, Description)
    #        ls[4] = stock_types (StockTypeID, Name, Description)
    #        ls[5] = strata (StratumID, Name, Description)
    #        ls[6] = secondary strata (SecondaryStratumID, Name, Description)
    #   if no parameters or table does not exist: Returns []
    #
    scenarios = db_query_general(sqlite_connection, 'Scenario_Names', project_id=project, table_name_project='SSim_Scenario', scenario_id=None, table_name_scenario=None)
    state_labels_x = db_query_general(sqlite_connection, 'StateLabelX',  project_id=project, table_name_project='STSim_StateLabelX', scenario_id=None, table_name_scenario=None)
    state_labels_y = db_query_general(sqlite_connection, 'StateLabelY',  project_id=project, table_name_project='STSim_StateLabelY', scenario_id=None, table_name_scenario=None)
    transition_groups = db_query_general(sqlite_connection, 'TransitionGroups',  project_id=project, table_name_project='STSim_TransitionGroup', scenario_id=None, table_name_scenario=None)
    if table_exists(sqlite_connection, 'SF_StockType'):
        stock_types = db_query_general(sqlite_connection, 'StockTypes',  project_id=project, table_name_project='SF_StockType', scenario_id=None, table_name_scenario=None)
    else:
        stock_types = []
    strata = db_query_general(sqlite_connection, 'Strata',  project_id=project, table_name_project='STSim_Stratum', scenario_id=None, table_name_scenario=None)
    if table_exists(sqlite_connection, 'STSim_SecondaryStratum'):
        secondary_strata = db_query_general(sqlite_connection, 'SecondaryStrata',  project_id=project, table_name_project='STSim_SecondaryStratum', scenario_id=None, table_name_scenario=None)
    else:
        secondary_strata = []


    return scenarios, state_labels_x, state_labels_y, transition_groups, stock_types, strata, secondary_strata