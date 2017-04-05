# **********************************************************
# ssim-functions.Python: Functions for the SSim package
# **********************************************************

# **********************************************************
# Setup
# **********************************************************

from ssim_api.ssim_add_external import add_scenario, index_exists, index_table
from ssim_api.ssim_general_functions import db_query_general

##Add StateClass Data
stateclass_csv_in = r"G:\2016_Working\jts_2016_09_01_LandCarbon_CDI\ssim_api_external_update\stateclass.csv"
sqlite_file = r"G:\2016_Working\jts_2016_09_01_LandCarbon_CDI\ssim_api_external_update\HawaiiLandCarbonAssessment.ssim"
output_table = 'STStim_OutputStratumState'#, 'WA_OutputStratumTransition']



add_scenario(stateclass_csv_in, output_table, sqlite_file, scenario_id=None)
#index_table(output_table, sqlite_file)
print("stateclass data loaded")

