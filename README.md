ssim_api
======================

This package provides functions for extracting results from the 
OutputStratumState, OutputStratumTransition, and OutputStock tables
in a .ssim database and paths to spatial results.

SETUP
=====
1. Package built with Python 3.5.1
2. Set up virtual environment with virtualenv (optional)
    - install virtual environment: pip install virtualenv  
    - create virtual environment: virtualenv <virtualenv name>
    - activate virtual environment: \path\to\virtualenv name\Scripts\activate  

3. Install package
    - install requirements: pip install pandas==0.18.0
    - download and unzip git file: https://gitlab.cr.usgs.gov/wgeogdev/ssim_api/repository/archive.zip?ref=master
	- python setup.py install
    
ABOUT THE CODE
==============
## The main functions in the package are stored in ssim_query_functions.py: 

1.	Functions, db_query_stateclass(), db_query_transitiongroup(), and db_query_stock() take a path to a .ssim database, and optional parameters for headers from the STSim_OutputStratumState, STSim_OutputStratumTransition, and SF_OutputStock tables respectively. Including parameters, as python tuples, limits results to the requested parameters. The functions dynamically build sql queries and apply them on the database. Results are returned as Pandas dataframes. 
2.	The functions query_spatial_files_stateclass(), query_spatial_files_tgap() built file paths to StateClass and Average Annual Transition Probability output tiffs. Results are returned as pandas dataframes
3.	The function project_summary() takes a .ssim connection and returns summary information on scenarios, stateclasses, transition groups, stock types, strata and secondary strata as a list of dataframes.  

Query_ssim_tabular.py, query_ssim_spatial.py, and squery_ssim_summary.py have examples of the above functions. 

## ssim_query_functions.py:  

<br>

**_db_query_stateclass(sqlite_connection, scenario_id =0, iteration=0, timestep=0, stratum=0, secondary_stratum = 0, state_label_x=0, state_label_y=0)**

Function for querying the STSim_OutputStratumState table in the database  
1. Args:  
    - sqlLiteConnection: connection to a SQLite database  
	- project_id: tuple with ProjectIDs for filtering query (optional - if not provided, all projects are included in results)
    - scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)  
    - iteration: tuple with iteration values for filtering query (optional - if not provided, all iterations are included in results)  
    - timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results)  
    - stratum: tuple with strata values for filtering query (optional - if not provided, all strata are included in results)  
    - secondary_stratum: tuple with secondary strata values for filtering query (optional - if not provided, all secoondary strata are included in results)  
    - state_label_x: tuple with state label x values for filtering query (optional - if not provided, all state label x are included in results)  
    - state_label_y: tuple with state label y values for filtering query (optional - if not provided, all state label y are included in results) 
    
2. Returns:  
    - dataframe with the results of the query  

<br><br>

 
**_db_query_transitiongroup(sqlite_connection, scenario_id=0, iteration=0, timestep=0, stratum=0, secondary_stratum = 0, transition_group=0)**
 
Function for querying the STSim_OutputStratumState table in the database  

1. Args:  
    - sqlLiteConnection: connection to a SQLite database 
	- project_id: tuple with ProjectIDs for filtering query (optional - if not provided, all projects are included in results)
    - scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)  
    - iteration: tuple with iteration values for filtering query (optional - if not provided, all iterations are included in results)  
    - timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results)  
    - stratum: tuple with strata values for filtering query (optional - if not provided, all strata are included in results)  
    - secondary_stratum: tuple with secondary strata values for filtering query (optional - if not provided, all secoondary strata are included in results)  
    - state_label_x: tuple with state label x values for filtering query (optional - if not provided, all state label x are included in results)  
    - state_label_y: tuple with state label y values for filtering query (optional - if not provided, all state label y are included in results)  
    
2. Returns:  
    - dataframe with the results of the query  
 
<br><br>
 

**_db_query_stock(sqlite_connection, scenario_id=0, iteration=0, timestep=0, stratum=0, secondary_stratum = 0, stateclass=0, stock_type=0)**

 Function for querying the STSim_OutputStratumState table in the database  
 
 1. Args:  
    - sqlLiteConnection: connection to a SQLite database  
	- project_id: tuple with ProjectIDs for filtering query (optional - if not provided, all projects are included in results)
    - scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)  
    - iteration: tuple with iteration values for filtering query (optional - if not provided, all iterations are included in results)  
    - timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results)  
    - stratum: tuple with strata values for filtering query (optional - if not provided, all strata are included in results)  
    - secondary_stratum: tuple with secondary strata values for filtering query (optional - if not provided, all secoondary strata are included in results)  
    - state_label_x: tuple with state label x values for filtering query (optional - if not provided, all state label x are included in results)  
    - state_label_y: tuple with state label y values for filtering query (optional - if not provided, all state label y are included in results)  
    
2. Returns:  
    - dataframe with the results of the query  
 
<br><br>

**_query_output_options(sqlite_connection, scenario_id=None)**  

Function for quering STSim_OutputOptions table
    
1. Args:   
    - sqlLiteConnection: connection to a SQLite database  
    - scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)  
    
2. Returns:  
    - dataframe with output options table
    

<br><br>

**_query_spatial_files_stateclass(sqlite_connection, scenario_id=None, iteration=None, timestep=None)**  

Function for quering spatial stateclass results  
    
1. Args:   
    - sqlLiteConnection: connection to a SQLite database  
    - scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)  
    - iteration: tuple with iteration values for filtering query (optional - if not provided, all iterations are included in results)  
    - timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results)  
    
2. Returns:  
    - dataframe with scenario_id, iteration, timestep, and path to state class spatial files
    
Assumes db.ssim.output folder is in the same directory as the database  


<br><br>

**_query_spatial_files_tgap(sqlite_connection, scenario_id=None, timestep=None, transition_group=None)**  

Function for quering average annual transition probability spatial results  
    
1. Args:   
    - sqlLiteConnection: connection to a SQLite database  
    - scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)   
    - timestep: tuple with timestep values for filtering query (optional - if not provided, all timesteps are included in results) 
	- transition_group: tuple with TransitionGroupIDs for filtering query (optional - if not provided, all timesteps are included in results)
    
2. Returns:  
    - dataframe with scenario_id, iteration, timestep, and path to spatial file
    
Assumes db.ssim.output folder is in the same directory as the database 

<br><br>

**_query_projects(sqlite_connection)**  

Function to get all project names and ids for a .ssim database
    
1. Args:   
    - sqlite_connection: path to sqLite db
    
2. Returns:  
    - a pandas dataframe with projectID and Name as headers
    
<br><br>

**_project_summary(sqlite_connection, project=None)**  

Creates a summary of parameters for from the sqlite database  

1. Args:  
   - sqlite_connection: path to sqLite db  
   - project_id: tuple with ProjectIDs for filtering query (optional - if not provided, all projects are included in results)
   
2. Returns:  
    - a list of pandas dataframes:  
        - ls[0] = scenarios  
        - ls[1] = state_labels_x  
        - ls[2] = state_labels_y  
        - ls[3] = transition_groups  
        - ls[4] = stock_types  
        - ls[5] = strata  
		- ls[6] = secondary_strata  
    - if no parameters or table does not exist: Returns []  

<br><br>

## ssim_general_functions.py contains several setup/helper functions, and a general query function:

<br>

## ssim_general_functions.py: 

<br>

**_db_query_general(sqlite_connection, query_name, project_id=None, table_name_project=None, scenario_id=None, table_name_scenario=None)**

Invokes an SQL query from a dictionary of queries on the sqlite database  
    
1. Args:  
    - sqlLiteConnection: connection to a SQLite database
    - query_name: name of query to apply stored in query_dictionary
    - project_id: tuple with projectIDs for filtering query (optional - if not provided, all projects are included in results)
	- table_name_project: table to filter by projectID (required if project_id is defined)
    - scenario_id: tuple with scenarioIDs for filtering query (optional - if not provided, all scenarios are included in results)
	- table_name_scenario: table to filter by ScenarioID (required if scenario_id is defined)
    
2. Returns:  
    - pandas dataframe with query results  
	
<br><br>
    
## ssim_postprocessing_functions.py contains two post-processing functions for pandas dataframes and functions to export as csv or json. 
1.	aggregate_over() takes a dataframe and sums a values column according to specified column headers.
2.	calculate_percentile() takes a dataframe and calculates a percentile for a defined parameter column and value column.
<br>

## ssim_postprocessing_functions.py.py: 
   
 <br><br>   
    
**_aggregate_over(df, aggregate_by_columns, values_column)**

function for aggregating values in one column over specified parameters within a pandas dataframe  
    
1. Args:  
    - df: A pandas dataframe  
    - aggregate_by_columns: tuple with column headings for columns to aggregate over  
    - value_column: column with values to sum  
     
2. Returns:  
    - a pandas dataframe with aggregated values  
    
    
 <br><br>   
    
    

**_calculate_percentile(df, percentile, values_column)**

function for calculating percentile for a column  
    
1. Args:  
    - df: input dataframe
    - csv_out: path to new csv ending in .csv
	
2. Returns:
    - csv file 
    
 <br><br>   
    
    

**_df_to_json(df, json_out=None)**

function for translating df to json
    
1. Args:  
    - df: input dataframe
    - json_out: optional path to output json file ending with .json
    
2. Returns:
    - json or optional json file  