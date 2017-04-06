# **********************************************************
# query_ssim_tabular.py: Example usage of db_query_stateclass(), db_query_transitiongroup(), db_query_stock()
# **********************************************************

# setup
from ssim_api.ssim_query_functions import db_query_stateclass, db_query_transitiongroup, db_query_stock
from ssim_api.ssim_postprocessing_functions import aggregate_over, calculate_percentile, df_to_csv
import time
import sqlite3

# **********************************************************
# Hawaii LandCarbon Assessment.ssim
# **********************************************************
# path to .ssim database
sqlite_file = r"/path/to/db.ssim"

#csvout
csv_out = r"/path/to/fileout.csv"

# define query vals
project_id = (7096,)
scenario_id = (6370,)
state_label_x = ("Forest","")
stratum = ("Dry",)
secondary_stratum = ("Hawai'i",)
timestep =(2015,)
group_by=("Timestep","Iteration")
# start timer
start = time.time()
percentile = ("Iteration", 95)
transition_group = ("test")

# run query and return pandas dataframe
# run  db_query_stateclass()
# returns:
    # dataframe with stateclass query results
StateClassOutput = db_query_stateclass(sqlite_file, project_id=project_id, scenario_id = scenario_id, state_label_x=None, stratum=stratum, secondary_stratum=None, group_by=None, percentile=None)
print("Stateclass query finished")

# run  db_query_transitiongroup(()
# returns:
    # dataframe with transitiongroup query results
TransitionGroupOutput = db_query_transitiongroup(sqlite_file, project_id=project_id, scenario_id = scenario_id, transition_group=None, stratum=None, secondary_stratum=None, group_by=group_by, percentile=percentile)
print("Transitiongroup query finished")

# run  db_query_stock()
# returns:
    # dataframe with stock query results
StockOutput = db_query_stock(sqlite_file, scenario_id=scenario_id, stratum= None, secondary_stratum=None, group_by=group_by, percentile=percentile)
#print("Stock query finished")


# export df to csv
#df_to_csv(StateClassOutput, csv_out)

# end timer
end = time.time()
print(end - start)
print("done")






