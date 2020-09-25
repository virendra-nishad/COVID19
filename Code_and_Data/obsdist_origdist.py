#!/usr/bin/env python3

import os
import json
import csv
import pandas
import numpy
import re
from mapping import correct_dist_map

file_name = "helper-data/obsdist-stateID/obsdist-stateID.csv"
obsdist_stateID_df = pandas.read_csv(file_name)


file_name = "helper-data/origdist-stateID/origdist-stateID.json"
in_file = open(file_name)
origdist_stateID_json = json.load(in_file)

obs_stateIDdist_list = list(obsdist_stateID_df["state_id/dist_name_at_portal"])

# prepare map from state and orig dist name to origdist name which is Qid one
stateIDorigdistname_origdist_dict = {}
for dist in origdist_stateID_json.keys():
    temp = dist.split('/')
    dist_name = origdist_stateID_json[dist] + "/" + temp[0]
    stateIDorigdistname_origdist_dict[dist_name] = dist
# print(stateIDorigdistname_origdist_dict)

stateIDorigdist_list = stateIDorigdistname_origdist_dict.keys()
# print(stateIDorigdist_list)

# map state name and dist name combination with origdist which also contains Q id as well
stateIDobsdist_origdist_map = {}
for dist in obs_stateIDdist_list:
    if dist in stateIDorigdist_list:
        stateIDobsdist_origdist_map[dist] = stateIDorigdistname_origdist_dict[dist]


folder_name = "helper-data/stateIDobsdist-origdistname"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
file_name = "helper-data/stateIDobsdist-origdistname/stateIDobsdist-origdistname.json"
with open(file_name, 'w') as fp_w:
    json.dump(stateIDobsdist_origdist_map, fp_w, indent=4)

# print("state_id/observed_dist_name combination mapped with district in modified neighbor")