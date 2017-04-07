# **********************************************************
# Example usage of the project_summary() function
# **********************************************************

# setup
from ssim_api.ssim_query_functions import project_summary, query_projects, query_output_options

# define connection to .ssim database
sqlite_file = r"/path/to/db.ssim"

# define query vals
project_id = (7096,)
scenario_id = (6370)

# run project_summary()
# Returns:
    #   A list of pandas dataframes:
    #        ls[0] = scenarios
    #        ls[1] = state_labels_x
    #        ls[2] = state_labels_y
    #        ls[3] = transition_groups
    #        ls[4] = stock_types
    #        ls[5] = strata
    #        ls[6] = secondary_strata

#ProjectSummary = project_summary(sqlite_file, project=project_id)
print("Project summary query finished")

# run query_projects()
# returns:
    # dataframe with project Names and IDs

Projects = query_projects(sqlite_file)
print("Projects query finished")

# run query_output_options()
# returns:
    # dataframe with output options

OutputOptions = query_output_options(sqlite_file, scenario_id = scenario_id)
print("Output options query finished")

print("done")

