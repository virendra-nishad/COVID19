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





file_name = "top-week.csv"
top_week_df = pandas.read_csv(file_name)
# print(top_month_df)

temp_df = top_week_df[top_week_df["method"] == "neighborhood"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

counter = 1
print("Top ", number_of_dist, " hotspot for week using neighborhood method :")
for indx in temphot_df.index:
    print(counter, ":", end='')
    counter += 1
    distid = "districtid"
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[temphot_df.loc[indx, temp_dist_id]], end=", ")
    print()
print()

counter = 1
print("Top", number_of_dist, "coldspot for week using neighborhood method: ")
for indx in tempcold_df.index:
    print(counter, ":", end='')
    counter += 1
    distid = "districtid"
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[tempcold_df.loc[indx, temp_dist_id]], end=", ")
    print()
print()


temp_df = top_week_df[top_week_df["method"] == "state"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]
# print(tempcold_df)

counter = 1
print("Top", number_of_dist, "hotspot for week using state method:")
for indx in temphot_df.index:
    print(counter, ":", end='')
    counter += 1
    distid = "districtid"
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[temphot_df.loc[indx, temp_dist_id]], end=", ")
    print()
print()

counter = 1
print("Top", number_of_dist, "coldspot for week using state method: ")
for indx in tempcold_df.index:
    print(counter, ":", end='')
    counter += 1
    distid = "districtid"
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[tempcold_df.loc[indx, temp_dist_id]], end=", ")
    print()
print()





file_name = "top-month.csv"
top_month_df = pandas.read_csv(file_name)
# print(top_month_df)

temp_df = top_month_df[top_month_df["method"] == "neighborhood"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

counter = 1
print("Top ", number_of_dist, " hotspot for month using neighborhood method :")
for indx in temphot_df.index:
    print(counter, ":", end='')
    counter += 1
    distid = "districtid"
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[temphot_df.loc[indx, temp_dist_id]], end=", ")
    print()
print()

counter = 1
print("Top", number_of_dist, "coldspot for month using neighborhood method: ")
for indx in tempcold_df.index:
    print(counter, ":", end='')
    counter += 1
    distid = "districtid"
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[tempcold_df.loc[indx, temp_dist_id]], end=", ")
    print()
print()


temp_df = top_month_df[top_month_df["method"] == "state"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]
# print(tempcold_df)

counter = 1
print("Top", number_of_dist, "hotspot for month using state method:")
for indx in temphot_df.index:
    print(counter, ":", end='')
    counter += 1
    distid = "districtid"
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[temphot_df.loc[indx, temp_dist_id]], end=", ")
    print()
print()

counter = 1
print("Top", number_of_dist, "coldspot for month using state method: ")
for indx in tempcold_df.index:
    print(counter, ":", end='')
    counter += 1
    distid = "districtid"
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[tempcold_df.loc[indx, temp_dist_id]], end=", ")
    print()
print()



file_name = "top-overall.csv"
top_overall_df = pandas.read_csv(file_name)

temp_df = top_overall_df[top_overall_df["method"] == "neighborhood"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

# print(temp_df)
# print(temphot_df)
# print(tempcold_df)

print("Top", number_of_dist, "hotspot ovearll using neighborhood method:")
distid = "districtid"
for indx in temphot_df.index:
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[temphot_df.loc[indx, temp_dist_id]], end=", ")
print()
print()

print("Top", number_of_dist, "coldspot overall using neighborhood method:")
distid = "districtid"
for indx in tempcold_df.index:
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[tempcold_df.loc[indx, temp_dist_id]], end=", ")
print()
print()





file_name = "top-overall.csv"
top_overall_df = pandas.read_csv(file_name)

temp_df = top_overall_df[top_overall_df["method"] == "state"]
temphot_df = temp_df[temp_df["spot"] == "hotspot"]
tempcold_df = temp_df[temp_df["spot"] == "coldspot"]

# print(temp_df)
# print(temphot_df)
# print(tempcold_df)

print("Top", number_of_dist, "hotspot ovearll using state method:")
distid = "districtid"
for indx in temphot_df.index:
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[temphot_df.loc[indx, temp_dist_id]], end=", ")
print()
print()

print("Top", number_of_dist, "coldspot overall using state method:")
distid = "districtid"
for indx in tempcold_df.index:
    for i in range(1, number_of_dist+1):
        temp_dist_id = distid + str(i)
        print(id_distname_dict[tempcold_df.loc[indx, temp_dist_id]], end=", ")
print()
print()