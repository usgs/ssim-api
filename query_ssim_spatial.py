# **********************************************************
# Example usage of the query_spatial_files_stateclass() function
# **********************************************************

# setup
from ssim_api.ssim_query_functions import query_spatial_files_stateclass, query_spatial_files_tgap
from ssim_api.ssim_postprocessing_functions import df_to_csv

# define .ssim connection
sqlite_file = r"/path/to/db.ssim"

#csvout
csv_out = r"/path/to/fileout.csv"

# define query vals
project_id = (7096,)
scenario_id = (6368, 6370)
iteration = (1,)
timestep=(2061,)
transition_group=(7129, 7141)

# run query_spatial_files_stateclass() function
# returns:
    #   A pandas dataframe with headers: ["Scenario", "Iteration", "Timestep", "Path"]
stateclass_paths = query_spatial_files_stateclass(sqlite_file, scenario_id=None, iteration=None, timestep=None)

# run query_spatial_files_tgap() function
# returns:
    #   A pandas dataframe with headers: ["Scenario", "Timestep", "TransitionGroupID", "Path"]
transitiongroup_paths = query_spatial_files_tgap(sqlite_file, scenario_id = scenario_id, timestep=timestep, transition_group=transition_group)

df_to_csv(transitiongroup_paths, csv_out)

print("Done")