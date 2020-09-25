#!/usr/bin/env python3

import csv
import json
import pandas

number_of_dist = 5

file_name = "origdist-id/origdist-id.json"
in_file = open(file_name)
origdist_id_json = json.load(in_file)
# print(origdist_id_json)

id_distname_dict = {}
for dist in origdist_id_json.keys():
    dist_name = dist.split('/')
    id_distname_dict[origdist_id_json[dist]] = dist_name[0]
# print(id_distname_dict)

file_name = "method-spot-week.csv"
top_week_df = pandas.read_csv(file_name)
# print(top_week_df)

temp_df = top_week_df[top_week_df["method"] == "neighborhood"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

print("Hotspot per week using neighborhood method")
for indx in temphot_df.index:
    distname = id_distname_dict[temphot_df.loc[indx, "districtid"]]
    print(temphot_df.loc[indx, "timeid"], temphot_df.loc[indx, "method"], temphot_df.loc[indx, "spot"], "\t", distname)
print()

print("Coldspot per week using neighborhood method")
for indx in tempcold_df.index:
    distname = id_distname_dict[tempcold_df.loc[indx, "districtid"]]
    print(tempcold_df.loc[indx, "timeid"], tempcold_df.loc[indx, "method"], tempcold_df.loc[indx, "spot"], "\t", distname)
print()

temp_df = top_week_df[top_week_df["method"] == "state"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

print("Hotspot per week using state method")
for indx in temphot_df.index:
    distname = id_distname_dict[temphot_df.loc[indx, "districtid"]]
    print(temphot_df.loc[indx, "timeid"], temphot_df.loc[indx, "method"], temphot_df.loc[indx, "spot"], "\t", distname)
print()

print("Coldspot per week using state method")
for indx in tempcold_df.index:
    distname = id_distname_dict[tempcold_df.loc[indx, "districtid"]]
    print(tempcold_df.loc[indx, "timeid"], tempcold_df.loc[indx, "method"], tempcold_df.loc[indx, "spot"], "\t", distname)
print()





file_name = "method-spot-month.csv"
top_month_df = pandas.read_csv(file_name)
# print(top_month_df)

temp_df = top_month_df[top_month_df["method"] == "neighborhood"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

print("Hotspot per month using neighborhood method")
for indx in temphot_df.index:
    distname = id_distname_dict[temphot_df.loc[indx, "districtid"]]
    print(temphot_df.loc[indx, "timeid"], temphot_df.loc[indx, "method"], temphot_df.loc[indx, "spot"], "\t", distname)
print()

print("Coldspot per month using neighborhood method")
for indx in tempcold_df.index:
    distname = id_distname_dict[tempcold_df.loc[indx, "districtid"]]
    print(tempcold_df.loc[indx, "timeid"], tempcold_df.loc[indx, "method"], tempcold_df.loc[indx, "spot"], "\t", distname)
print()

temp_df = top_month_df[top_month_df["method"] == "state"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

print("Hotspot per month using state method")
for indx in temphot_df.index:
    distname = id_distname_dict[temphot_df.loc[indx, "districtid"]]
    print(temphot_df.loc[indx, "timeid"], temphot_df.loc[indx, "method"], temphot_df.loc[indx, "spot"], "\t", distname)
print()

print("Coldspot per month using state method")
for indx in tempcold_df.index:
    distname = id_distname_dict[tempcold_df.loc[indx, "districtid"]]
    print(tempcold_df.loc[indx, "timeid"], tempcold_df.loc[indx, "method"], tempcold_df.loc[indx, "spot"], "\t", distname)
print()








file_name = "method-spot-overall.csv"
top_overall_df = pandas.read_csv(file_name)
# print(top_month_df)

temp_df = top_overall_df[top_overall_df["method"] == "neighborhood"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

print("Hotspot overall using neighborhood method")
for indx in temphot_df.index:
    distname = id_distname_dict[temphot_df.loc[indx, "districtid"]]
    print(temphot_df.loc[indx, "timeid"], temphot_df.loc[indx, "method"], temphot_df.loc[indx, "spot"], "\t", distname)
print()

print("Coldspot overall using neighborhood method")
for indx in tempcold_df.index:
    distname = id_distname_dict[tempcold_df.loc[indx, "districtid"]]
    print(tempcold_df.loc[indx, "timeid"], tempcold_df.loc[indx, "method"], tempcold_df.loc[indx, "spot"], "\t", distname)
print()

temp_df = top_overall_df[top_overall_df["method"] == "state"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

print("Hotspot overall using state method")
for indx in temphot_df.index:
    distname = id_distname_dict[temphot_df.loc[indx, "districtid"]]
    print(temphot_df.loc[indx, "timeid"], temphot_df.loc[indx, "method"], temphot_df.loc[indx, "spot"], "\t", distname)
print()

print("Coldspot overall using state method")
for indx in tempcold_df.index:
    distname = id_distname_dict[tempcold_df.loc[indx, "districtid"]]
    print(tempcold_df.loc[indx, "timeid"], tempcold_df.loc[indx, "method"], tempcold_df.loc[indx, "spot"], "\t", distname)
print()