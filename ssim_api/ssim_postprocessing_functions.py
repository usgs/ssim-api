# **********************************************************
# Setup
# **********************************************************
import pandas as pd
# **********************************************************
# Post-procesing functions for pandas dataframes
# **********************************************************

def aggregate_over(df, aggregate_by_columns, values_column):
    # function for aggregating values in one column over specified parameters within a pandas dataframe
    #
    # Args:
    #   df: A pandas dataframe
    #   aggregate_by_columns: tuple with column headings for columns to aggregate over
    #   value_column: column with values to sum
    #
    # Returns:
    #   A pandas dataframe with aggregated values
    #
    col_headings = df.columns
    print("Sum by: " + str(aggregate_by_columns))
    aggregate_by_columns.append(values_column)
    col_headings = [x for x in col_headings if x not in aggregate_by_columns]
    df = df.groupby(col_headings, as_index=False)[values_column].sum()
    return df

def calculate_percentile(df, percentile, values_column):
    # function for calculating percentile for a column
    #
    # Args:
    #   df: A pandas dataframe
    #   percentile: tuple with three values: (character for column name to calculate percentile over, percentil low, percentile high)
    #   value_column: character for column with values to calcalate percentile with
    #
    # Returns:
    #   A pandas dataframe with Min, Mean, and Max specified
    #
    print("Calculating percentile for: " + str(percentile))
    col_headings = df.columns
    remove_headings = [percentile[0], values_column]
    col_headings = [x for x in col_headings if x not in remove_headings]
    df = df.groupby(col_headings, as_index=False)[values_column].quantile([percentile[1], 0.5, percentile[2]]).reset_index()
    df.columns = col_headings + ['Min', 'Mean', 'Max']
    return df

# **********************************************************
# Dataframe export functions
# **********************************************************

def df_to_csv(df, csv_out):
    # Creates csv from dataframe
    #
    # Args:
    #   df: input dataframe
    #   csv_out: path to new csv ending in .csv
    #
    # Returns:
    #   csv
    #
    df.to_csv(csv_out, encoding='utf-8')

def df_to_json(df, json_out=None):
    # Creates json from dataframe
    #
    # Args:
    #   df: input dataframe
    #   json_out: optional path to output json file ending with .json
    #
    # Returns:
    #   json
    #
    if json_out == None:
        return df.reset_index().to_json(orient='records')
    else:
        text_file = open(json_out, "w")
        text_file.write(df.reset_index().to_json(orient='records'))
        text_file.close()