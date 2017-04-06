# **********************************************************
# ssim-functions.Python: Functions for the SSim package
# **********************************************************

# **********************************************************
# Setup
# **********************************************************

from ssim_api.ssim_data_functions import add_scenario, index_exists, index_table, remove_scenario
from ssim_api.ssim_general_functions import db_query_general

##Add StateClass Data
stateclass_csv_in = r"path\to\csv"
sqlite_file = r"path\tp\database"
output_table = 'STSim_OutputStratumState'#, 'WA_OutputStratumTransition']


#add_scenario(stateclass_csv_in, output_table, sqlite_file, scenario_id=None)

print("stateclass data loaded")

remove_scenario(sqlite_file, output_table, '6386')

index_table(output_table, sqlite_file)