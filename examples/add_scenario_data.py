# **********************************************************
# ssim-functions.Python: Functions for the SSim package
# **********************************************************

# **********************************************************
# Setup
# **********************************************************

from ssim_api.ssim_add_data_functions import remove_scenario, add_scenario_data


##Add StateClass Data
csv_in = r"path\to\csv"
sqlite_file = r"path\to\sqlitedb"
data_type = "transition" #stateclass or stock
scenario = '9999'


#add_scenario_data(csv_in, sqlite_file, data_type, index=True)

remove_scenario(sqlite_file, data_type, scenario)

