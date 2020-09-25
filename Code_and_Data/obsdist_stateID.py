#!/usr/bin/env python3

import os
import json
import csv
import re
import pandas
import numpy
import re


# read unique district from portal
# convert to lower and insert _ as where ever appropriate
# store in sorted order in helper data


# loading main data
parent_dir = os.getcwd()
file_name =  parent_dir + "/covid19data-json/data.json"
in_file = open(file_name)
orig_data_json = json.load(in_file)

unique_dist_in_data_set = set()

for date in orig_data_json.keys():
    for state in orig_data_json[date].keys():
        if "districts" in orig_data_json[date][state].keys():
            for dist in orig_data_json[date][state]["districts"].keys():
                temp = dist + '/' + state
                unique_dist_in_data_set.add(temp)


cols = ["dist_name_at_portal","dist_transformed_name", "state_id", "state_id/dist_transformed_name", "state_id/dist_name_at_portal"]
idx = numpy.array(numpy.arange(len(unique_dist_in_data_set)))
data = numpy.zeros(shape=(len(unique_dist_in_data_set), len(cols)))
obs_dist_1_df = pandas.DataFrame(data, index=idx, columns=cols)

obs_dist_list = []
for dist in unique_dist_in_data_set:
    obs_dist_list.append(dist)

# sorting
obs_dist_list = sorted(obs_dist_list)

idx = 0
for dist in obs_dist_list:
    temp = dist.split('/')
    new_dist = temp[0]
    new_dist = new_dist.lower()
    new_dist =  re.sub('[^0-9a-z]+', '_', new_dist)

    obs_dist_1_df.loc[idx, "dist_name_at_portal"] = temp[0]
    obs_dist_1_df.loc[idx, "dist_transformed_name"] = new_dist
    obs_dist_1_df.loc[idx, "state_id"] = temp[1]
    obs_dist_1_df.loc[idx, "state_id/dist_transformed_name"] = temp[1] + "/" + new_dist
    obs_dist_1_df.loc[idx, "state_id/dist_name_at_portal"] = temp[1] + "/" + temp[0]
    idx += 1
# print(obs_dist_1_df)

helper_folder = parent_dir + "/helper-data/"
if not os.path.exists(helper_folder):
    os.mkdir(helper_folder)

out_csv_folder = parent_dir + "/helper-data/obsdist-stateID/"
if not os.path.exists(out_csv_folder):
    os.mkdir(out_csv_folder)
out_csv_file = parent_dir + "/helper-data/obsdist-stateID/obsdist-stateID.csv"
obs_dist_1_df.to_csv(out_csv_file, index=False)

# print("saved meta of observed district at portal as -> helper-data/obsdist-stateID/obsdist-stateID.csv")