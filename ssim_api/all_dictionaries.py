
# **********************************************************
#  Dictionary to store SQL queries
# **********************************************************
query_dictionary = {
'OutputStratumState_query': '''SELECT SSim_Scenario.ProjectID, STSim_OutputStratumState.ScenarioID, STSim_OutputStratumState.Iteration, STSim_OutputStratumState.Timestep, STSim_Stratum.Name AS Stratum, STSim_SecondaryStratum.Name AS SecondaryStratum, STSim_StateLabelX.Name AS StateLabelX, STSim_StateLabelY.Name AS StateLabelY, STSim_OutputStratumState.AgeMin, STSim_OutputStratumState.AgeMax, STSim_OutputStratumState.Amount FROM ((((STSim_OutputStratumState INNER JOIN STSim_Stratum ON STSim_OutputStratumState.StratumID = STSim_Stratum.StratumID) INNER JOIN STSim_SecondaryStratum ON STSim_OutputStratumState.SecondaryStratumID = STSim_SecondaryStratum.SecondaryStratumID) INNER JOIN STSim_StateClass ON STSim_OutputStratumState.StateClassID = STSim_StateClass.StateClassID) INNER JOIN STSim_StateLabelX ON (STSim_StateClass.StateLabelXID = STSim_StateLabelX.StateLabelXID) AND (STSim_StateClass.ProjectID = STSim_StateLabelX.ProjectID)) INNER JOIN STSim_StateLabelY ON (STSim_StateClass.StateLabelYID = STSim_StateLabelY.StateLabelYID) AND (STSim_StateClass.ProjectID = STSim_StateLabelY.ProjectID) INNER JOIN SSim_Scenario ON (STSim_OutputStratumState.ScenarioID = SSim_Scenario.ScenarioID)''',
'OutputStratumTransition_query': '''SELECT SSim_Scenario.ProjectID, STSim_OutputStratumTransition.ScenarioID, STSim_OutputStratumTransition.Iteration, STSim_OutputStratumTransition.Timestep, STSim_Stratum.Name AS Stratum, STSim_SecondaryStratum.Name AS SecondaryStratum, STSim_TransitionGroup.Name AS TransitionGroup, STSim_OutputStratumTransition.AgeMin, STSim_OutputStratumTransition.AgeMax, STSim_OutputStratumTransition.Amount FROM (((STSim_OutputStratumTransition INNER JOIN STSim_Stratum ON STSim_OutputStratumTransition.StratumID = STSim_Stratum.StratumID) INNER JOIN STSim_SecondaryStratum ON STSim_OutputStratumTransition.SecondaryStratumID = STSim_SecondaryStratum.SecondaryStratumID) INNER JOIN STSim_TransitionGroup ON STSim_OutputStratumTransition.TransitionGroupID = STSim_TransitionGroup.TransitionGroupID) INNER JOIN SSim_Scenario ON STSim_OutputStratumTransition.ScenarioID = SSim_Scenario.ScenarioID ''',
'OutputStock_query':'''SELECT SSim_Scenario.ProjectID, SF_OutputStock.ScenarioID, SF_OutputStock.Iteration, SF_OutputStock.Timestep, STSim_Stratum.Name AS Stratum, STSim_SecondaryStratum.Name AS SecondaryStratum, STSim_StateClass.Name AS StateClass, SF_StockType.Name AS StockType, SF_OutputStock.Amount FROM ((((SF_OutputStock INNER JOIN STSim_Stratum ON SF_OutputStock.StratumID = STSim_Stratum.StratumID) INNER JOIN STSim_SecondaryStratum ON SF_OutputStock.SecondaryStratumID = STSim_SecondaryStratum.SecondaryStratumID) INNER JOIN STSim_StateClass ON SF_OutputStock.StateClassID = STSim_StateClass.StateClassID) INNER JOIN SF_StockType ON SF_OutputStock.StockTypeID = SF_StockType.StockTypeID) INNER JOIN SSim_Scenario ON SF_OutputStock.ScenarioID = SSim_Scenario.ScenarioID''',
'Scenario_Names': '''SELECT SSim_Scenario.Name, SSim_Scenario.ScenarioID, SSim_Scenario.RunStatus, STSim_RunControl.MaximumIteration, STSim_RunControl.MaximumTimestep, STSim_RunControl.MinimumIteration, STSim_RunControl.MinimumTimestep, STSim_RunControl.IsSpatial FROM (SSim_Scenario INNER JOIN STSim_RunControl ON SSim_Scenario.ScenarioID = STSim_RunControl.ScenarioID) ''',
'Project_Ids': '''SELECT Name, ProjectID FROM SSim_Project''',
'Scenario_Names_All': '''SELECT Name, ScenarioID FROM SSim_Scenario''',
'StateLabelX': '''SELECT StateLabelXID, Name, Description FROM STSim_StateLabelX''',
'StateLabelY': '''SELECT StateLabelYID, Name, Description FROM STSim_StateLabelY''',
'TransitionGroups': '''SELECT TransitionGroupID, Name, Description FROM STSim_TransitionGroup''',
'StockTypes': '''SELECT StockTypeID, Name, Description FROM SF_StockType''',
'TableExists': '''SELECT Name FROM sqlite_master WHERE type = "table" AND name = ?''',
'Strata': '''SELECT StratumID, Name, Description FROM STSim_Stratum''',
'SecondaryStrata': '''SELECT SecondaryStratumID, Name, Description FROM STSim_SecondaryStratum''',
'RunControl': '''SELECT ScenarioID, MaximumIteration, MaximumTimestep, IsSpatial FROM STSim_RunControl''',
'OutputOptions': '''SELECT * FROM STSim_OutputOptions'''
}



