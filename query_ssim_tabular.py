# **********************************************************
# query_ssim_tabular.py: Example usage of db_query_stateclass(), db_query_transitiongroup(), db_query_stock()
# **********************************************************

# setup
from ssim_api.ssim_query_functions import db_query_stateclass, db_query_transitiongroup, db_query_stock
from ssim_api.ssim_postprocessing_functions import aggregate_over, calculate_percentile, df_to_csv
import time

# **********************************************************
# Hawaii LandCarbon Assessment.ssim
# **********************************************************
# path to .ssim database
sqlite_file = r"/path/to/db.ssim"

#csvout
csv_out = r"/path/to/fileout.csv"

# define query vals
project_id = (7096,)
scenario_id = (6368, 6370)
state_label_x = ("Forest","Grassland")
stratum = ("Dry","Wet","Mesic")
secondary_stratum = ("Hawai'i", "Maiu", "O'ahu")
timestep =(2015,)

# start timer
start = time.time()

# run query and return pandas dataframe
# run  db_query_stateclass()
# returns:
    # dataframe with stateclass query results
StateClassOutput = db_query_stateclass(sqlite_file, state_label_x=state_label_x, stratum=stratum,project_id=project_id, scenario_id = scenario_id, timestep=timestep)
print("Stateclass query finished")
# run  db_query_transitiongroup(()
# returns:
    # dataframe with transitiongroup query results
TransitionGroupOutput = db_query_transitiongroup(sqlite_file, project_id=project_id, timestep=timestep)
print("Transitiongroup query finished")
# run  db_query_stock()
# returns:
    # dataframe with stock query results
StockOutput = db_query_stock(sqlite_file, scenario_id=scenario_id, stratum= stratum, secondary_stratum=secondary_stratum)
print("Stock query finished")

#define variables to aggregate over and return aggregated values
aggregate_by_columns = ["AgeMin", "AgeMax", 'SecondaryStratum']
column = "Amount"
StateClassOutput = aggregate_over(StateClassOutput, aggregate_by_columns, column)

# define percentile variables and return percentile values
percentile = ["Iteration", 0.05, 0.95]
StateClassOutput = calculate_percentile(StateClassOutput, percentile, column)

# export df to csv
df_to_csv(StateClassOutput, csv_out)

# end timer
end = time.time()
print(end - start)
print("done")






