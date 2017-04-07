
# **********************************************************
#  Dictionary to store SQL queries
# **********************************************************
query_dictionary = {
'OutputStratumState_query_from':''' FROM ((((STSim_OutputStratumState INNER JOIN STSim_Stratum ON STSim_OutputStratumState.StratumID = STSim_Stratum.StratumID) INNER JOIN STSim_SecondaryStratum ON STSim_OutputStratumState.SecondaryStratumID = STSim_SecondaryStratum.SecondaryStratumID) INNER JOIN STSim_StateClass ON STSim_OutputStratumState.StateClassID = STSim_StateClass.StateClassID) INNER JOIN STSim_StateLabelX ON (STSim_StateClass.StateLabelXID = STSim_StateLabelX.StateLabelXID) AND (STSim_StateClass.ProjectID = STSim_StateLabelX.ProjectID)) INNER JOIN STSim_StateLabelY ON (STSim_StateClass.StateLabelYID = STSim_StateLabelY.StateLabelYID) AND (STSim_StateClass.ProjectID = STSim_StateLabelY.ProjectID) INNER JOIN SSim_Scenario ON (STSim_OutputStratumState.ScenarioID = SSim_Scenario.ScenarioID)''',
'OutputStratumTransition_query_from': ''' FROM (((STSim_OutputStratumTransition INNER JOIN STSim_Stratum ON STSim_OutputStratumTransition.StratumID = STSim_Stratum.StratumID) INNER JOIN STSim_SecondaryStratum ON STSim_OutputStratumTransition.SecondaryStratumID = STSim_SecondaryStratum.SecondaryStratumID) INNER JOIN STSim_TransitionGroup ON STSim_OutputStratumTransition.TransitionGroupID = STSim_TransitionGroup.TransitionGroupID) INNER JOIN SSim_Scenario ON STSim_OutputStratumTransition.ScenarioID = SSim_Scenario.ScenarioID''',
'OutputStock_query_from':''' FROM ((((SF_OutputStock INNER JOIN STSim_Stratum ON SF_OutputStock.StratumID = STSim_Stratum.StratumID) INNER JOIN STSim_SecondaryStratum ON SF_OutputStock.SecondaryStratumID = STSim_SecondaryStratum.SecondaryStratumID) INNER JOIN STSim_StateClass ON SF_OutputStock.StateClassID = STSim_StateClass.StateClassID) INNER JOIN SF_StockType ON SF_OutputStock.StockTypeID = SF_StockType.StockTypeID) INNER JOIN SSim_Scenario ON SF_OutputStock.ScenarioID = SSim_Scenario.ScenarioID''',
'Scenario_Names': '''SELECT SSim_Scenario.Name, SSim_Scenario.ScenarioID, SSim_Scenario.RunStatus, STSim_RunControl.MaximumIteration, STSim_RunControl.MaximumTimestep, STSim_RunControl.MinimumIteration, STSim_RunControl.MinimumTimestep, STSim_RunControl.IsSpatial FROM (SSim_Scenario INNER JOIN STSim_RunControl ON SSim_Scenario.ScenarioID = STSim_RunControl.ScenarioID) ''',
'Project_Ids': '''SELECT Name, ProjectID FROM SSim_Project''',
'Scenario_Names_All': '''SELECT Name, ScenarioID FROM SSim_Scenario''',
'StateLabelX': '''SELECT StateLabelXID, Name, Description FROM STSim_StateLabelX''',
'StateLabelY': '''SELECT StateLabelYID, Name, Description FROM STSim_StateLabelY''',
'StateClass': '''SELECT StateClassID, Name, Description FROM STSim_StateClass''',
'TransitionGroups': '''SELECT TransitionGroupID, Name, Description FROM STSim_TransitionGroup''',
'StockTypes': '''SELECT StockTypeID, Name, Description FROM SF_StockType''',
'TableExists': '''SELECT Name FROM sqlite_master WHERE type = "table" AND name = ?''',
'Strata': '''SELECT StratumID, Name, Description FROM STSim_Stratum''',
'SecondaryStrata': '''SELECT SecondaryStratumID, Name, Description FROM STSim_SecondaryStratum''',
'RunControl': '''SELECT ScenarioID, MaximumIteration, MaximumTimestep, IsSpatial FROM STSim_RunControl''',
'OutputOptions': '''SELECT * FROM STSim_OutputOptions'''
}



select_dic = {
"OutputStratumState_select_dic":{'IDProject': 'SSim_Scenario.ProjectID AS IDProject', 'IDScenario': 'STSim_OutputStratumState.ScenarioID AS IDScenario', 'Iteration': 'STSim_OutputStratumState.Iteration AS Iteration', 'Timestep': 'STSim_OutputStratumState.Timestep AS Timestep', 'Stratum': 'STSim_Stratum.Name AS Stratum', 'SecondaryStratum': 'STSim_SecondaryStratum.Name AS SecondaryStratum', 'StateLabelX': 'STSim_StateLabelX.Name AS StateLabelX', 'StateLabelY': 'STSim_StateLabelY.Name AS StateLabelY', 'AgeMin': 'STSim_OutputStratumState.AgeMin AS AgeMin', 'AgeMax': 'STSim_OutputStratumState.AgeMax AS AgeMax', 'Amount':  'STSim_OutputStratumState.Amount AS Amount'},
"OutputStratumTransition_select_dic":{'IDProject': 'SSim_Scenario.ProjectID AS IDProject', 'IDScenario':'STSim_OutputStratumTransition.ScenarioID AS IDScenario', 'Iteration': 'STSim_OutputStratumTransition.Iteration AS Iteration', 'Timestep': 'STSim_OutputStratumTransition.Timestep AS Timestep', 'Stratum': 'STSim_Stratum.Name AS Stratum', 'SecondaryStratum': 'STSim_SecondaryStratum.Name AS SecondaryStratum', 'TransitionGroup': 'STSim_TransitionGroup.Name AS TransitionGroup', 'AgeMin': 'STSim_OutputStratumTransition.AgeMin AS AgeMin', 'AgeMax': 'STSim_OutputStratumTransition.AgeMax AS AgeMax', 'Amount':  'STSim_OutputStratumTransition.Amount AS Amount'},
"OutputStock_query_select_dic": {'IDProject': 'SSim_Scenario.ProjectID AS IDProject', 'IDScenario': 'SF_OutputStock.ScenarioID AS IDScenario', 'Iteration': 'SF_OutputStock.Iteration AS Iteration', 'Timestep':'SF_OutputStock.Timestep AS Timestep', 'Stratum': 'STSim_Stratum.Name AS Stratum', 'SecondaryStratum': 'STSim_SecondaryStratum.Name AS SecondaryStratum', 'StateClass': 'STSim_StateClass.Name AS StateClass', 'StockType':'SF_StockType.Name AS StockType', 'Amount': 'SF_OutputStock.Amount AS Amount'},
}

table_name_dic = {
"stateclass": "STSim_OutputStratumState",
"transition": "STSim_OutputStratumTransition",
"stock": "SF_OutputStock"
}

table_insert_dic = {
"STSim_OutputStratumState": 'INSERT INTO %s (ScenarioID, Iteration, Timestep, StratumID, SecondaryStratumID, StateClassID, StateLabelXID, StateLabelYID, AgeMin, AgeMax, AgeClass, Amount) VALUES (%s)',
"STSim_OutputStratumTransition": 'INSERT INTO %s (ScenarioID, Iteration, Timestep, StratumID, SecondaryStratumID, TransitionGroupID, AgeMin, AgeMax, AgeClass, Amount) VALUES (%s)',
"SF_OutputStock": 'INSERT INTO %s (ScenarioID, Iteration, Timestep, StratumID, SecondaryStratumID, StateClassID, StockTypeID, Amount) VALUES (%s)'
}