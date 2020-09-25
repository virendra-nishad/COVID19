#!/usr/bin/env python3

import json
import csv
import pandas
import os
import matplotlib.pyplot as plt


file_name = "origdist-id/origdist-id.json"
in_file = open(file_name)
origdist_id_json = json.load(in_file)

id_distname_dict = {}
for dist in origdist_id_json.keys():
    dist_name = dist.split('/')
    id_distname_dict[origdist_id_json[dist]] = dist_name[0]

filename = "method-spot-week.csv"
df = pandas.read_csv(filename)
# print(df)

hotspot_dist_count = []
# print("Hot spot count: neighborhood")
for time_id in range(1, 26):
    temp_df = df[(df["timeid"] == time_id) & (df["spot"] == "hotspot") & (df["method"] == "neighborhood")]

    hotspot_dist_count.append(temp_df.shape[0])
    x_data = list(range(1, 26))

fig = plt.bar(x_data, hotspot_dist_count)
plt.title("Number of hotspot per week using neighborhood method")
plt.ylabel("number of hotspot")
plt.xlabel("week number")
parent_dir = os.getcwd()
path = os.path.join(parent_dir, "plot-hotspot-count")
if not os.path.exists(path):
    os.mkdir(path)
fig_name = "weekly_hotspot_neighborhood.png"
plt.savefig(os.path.join(path, fig_name))
plt.clf()
# print(hotspot_dist_count)


# print("Hot spot count: state")
hotspot_dist_count = []
for time_id in range(1, 26):
    temp_df = df[(df["timeid"] == time_id) & (df["spot"] == "hotspot") & (df["method"] == "state")]
    # print(temp_df)
    hotspot_dist_count.append(temp_df.shape[0])
    x_data = list(range(1, 26))

fig = plt.bar(x_data, hotspot_dist_count)
plt.title("Number of hotspot per week using state method")
plt.ylabel("number of hotspot")
plt.xlabel("week number")
parent_dir = os.getcwd()
path = os.path.join(parent_dir, "plot-hotspot-count")
if not os.path.exists(path):
    os.mkdir(path)
fig_name = "weekly_hotspot_state.png"
plt.savefig(os.path.join(path, fig_name))
plt.clf()


filename = "method-spot-month.csv"
df = pandas.read_csv(filename)
# print(df)

# print("Hot spot count: neighborhood")
hotspot_dist_count = []
for time_id in range(1, 8):
    temp_df = df[(df["timeid"] == time_id) & (df["spot"] == "hotspot") & (df["method"] == "neighborhood")]
    # print(temp_df)
    hotspot_dist_count.append(temp_df.shape[0])
    x_data = list(range(1, 8))

fig = plt.bar(x_data, hotspot_dist_count)
plt.title("Number of hotspot per month using neighborhood method")
plt.ylabel("number of hotspot")
plt.xlabel("month number")
parent_dir = os.getcwd()
path = os.path.join(parent_dir, "plot-hotspot-count")
if not os.path.exists(path):
    os.mkdir(path)
fig_name = "monthly_hotspot_neighborhood.png"
plt.savefig(os.path.join(path, fig_name))
plt.clf()


# print("Hot spot count: state")
hotspot_dist_count = []
for time_id in range(1,8):
    temp_df = df[(df["timeid"] == time_id) & (df["spot"] == "hotspot") & (df["method"] == "state")]
    # print(temp_df)
    hotspot_dist_count.append(temp_df.shape[0])
    x_data = list(range(1, 8))

fig = plt.bar(x_data, hotspot_dist_count)
plt.title("Number of hotspot per month using state method")
plt.ylabel("number of hotspot")
plt.xlabel("month number")
parent_dir = os.getcwd()
path = os.path.join(parent_dir, "plot-hotspot-count")
if not os.path.exists(path):
    os.mkdir(path)
fig_name = "monthly_hotspot_state.png"
plt.savefig(os.path.join(path, fig_name))
plt.clf()