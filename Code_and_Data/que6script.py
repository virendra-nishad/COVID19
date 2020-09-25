#!/usr/bin/env python3

import json
import csv
import pandas

file_name = "cases-week.csv"
cases_week_df = pandas.read_csv(file_name)
# print(cases_week_df)

file_name = "neighbor-week.csv"
neighbor_week_df = pandas.read_csv(file_name)
neighbor_week_df = neighbor_week_df.set_index(["districtid", "week"])
# print(neighbor_week_df)

file_name = "state-week.csv"
state_week_df = pandas.read_csv(file_name)
state_week_df = state_week_df.set_index(["districtid", "week"])
# print(state_week_df)


cases_week_df["neighborhoodzscore"] = 0
cases_week_df["statezscore"] = 0

for idx in cases_week_df.index:
    districtid = cases_week_df.loc[idx, "districtid"]
    week = cases_week_df.loc[idx, "week"]
    cases = cases_week_df.loc[idx, "cases"]

    nei_mean = neighbor_week_df.loc[(districtid, week), "neighbormean"]
    nei_stdev = neighbor_week_df.loc[(districtid, week), "neighborstdev"]

    state_mean = state_week_df.loc[(districtid, week), "statemean"]
    state_stdev = state_week_df.loc[(districtid, week), "statestdev"]

    neighborhoodzscore = 0
    statezscore = 0

    if nei_stdev == 0:
        neighborhoodzscore = 0
    else:
        neighborhoodzscore = (cases - nei_mean) / nei_stdev

    if state_stdev == 0:
        statezscore = 0
    else:
        statezscore = (cases - state_mean) / state_stdev
    
    cases_week_df.loc[idx, "neighborhoodzscore"] = float("{:.2f}".format(neighborhoodzscore))
    cases_week_df.loc[idx, "statezscore"] = float("{:.2f}".format(statezscore))

del cases_week_df["cases"]

# print(cases_week_df)
cases_week_df.to_csv("zscore-week.csv", index=False)
# print("zscore-week.csv -> created")






file_name = "cases-month.csv"
cases_month_df = pandas.read_csv(file_name)
# print(cases_week_df)

file_name = "neighbor-month.csv"
neighbor_month_df = pandas.read_csv(file_name)
neighbor_month_df = neighbor_month_df.set_index(["districtid", "month"])
# print(neighbor_week_df)

file_name = "state-month.csv"
state_month_df = pandas.read_csv(file_name)
state_month_df = state_month_df.set_index(["districtid", "month"])
# print(state_week_df)


cases_month_df["neighborhoodzscore"] = 0
cases_month_df["statezscore"] = 0

for idx in cases_month_df.index:
    districtid = cases_month_df.loc[idx, "districtid"]
    month = cases_month_df.loc[idx, "month"]
    cases = cases_month_df.loc[idx, "cases"]

    nei_mean = neighbor_month_df.loc[(districtid, month), "neighbormean"]
    nei_stdev = neighbor_month_df.loc[(districtid, month), "neighborstdev"]

    state_mean = state_month_df.loc[(districtid, month), "statemean"]
    state_stdev = state_month_df.loc[(districtid, month), "statestdev"]

    neighborhoodzscore = 0
    statezscore = 0

    if nei_stdev == 0:
        neighborhoodzscore = 0
    else:
        neighborhoodzscore = (cases - nei_mean) / nei_stdev

    if state_stdev == 0:
        statezscore = 0
    else:
        statezscore = (cases - state_mean) / state_stdev
    
    cases_month_df.loc[idx, "neighborhoodzscore"] = float("{:.2f}".format(neighborhoodzscore))
    cases_month_df.loc[idx, "statezscore"] = float("{:.2f}".format(statezscore))

del cases_month_df["cases"]

# print(cases_month_df)
cases_month_df.to_csv("zscore-month.csv", index=False)
# print("zscore-month.csv -> created")





file_name = "cases-overall.csv"
cases_overall_df = pandas.read_csv(file_name)
# print(cases_week_df)

file_name = "neighbor-overall.csv"
neighbor_overall_df = pandas.read_csv(file_name)
neighbor_overall_df = neighbor_overall_df.set_index(["districtid", "overall"])
# print(neighbor_week_df)

file_name = "state-overall.csv"
state_overall_df = pandas.read_csv(file_name)
state_overall_df = state_overall_df.set_index(["districtid", "overall"])
# print(state_week_df)


cases_overall_df["neighborhoodzscore"] = 0
cases_overall_df["statezscore"] = 0

for idx in cases_overall_df.index:
    districtid = cases_overall_df.loc[idx, "districtid"]
    overall = cases_overall_df.loc[idx, "overall"]
    cases = cases_overall_df.loc[idx, "cases"]

    nei_mean = neighbor_overall_df.loc[(districtid, overall), "neighbormean"]
    nei_stdev = neighbor_overall_df.loc[(districtid, overall), "neighborstdev"]

    state_mean = state_overall_df.loc[(districtid, overall), "statemean"]
    state_stdev = state_overall_df.loc[(districtid, overall), "statestdev"]

    neighborhoodzscore = 0
    statezscore = 0
    
    if nei_stdev == 0:
        neighborhoodzscore = 0
    else:
        neighborhoodzscore = (cases - nei_mean) / nei_stdev

    if state_stdev == 0:
        statezscore = 0
    else:
        statezscore = (cases - state_mean) / state_stdev
    
    cases_overall_df.loc[idx, "neighborhoodzscore"] = float("{:.2f}".format(neighborhoodzscore))
    cases_overall_df.loc[idx, "statezscore"] = float("{:.2f}".format(statezscore))

del cases_overall_df["cases"]

# print(cases_overall_df)
cases_overall_df.to_csv("zscore-overall.csv", index=False)
# print("zscore-overall.csv -> created")