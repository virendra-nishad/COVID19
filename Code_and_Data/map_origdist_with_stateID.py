#!/usr/bin/env python3

import os
import json
import csv
import pandas
import numpy
from mapping import dist_to_stateID

# This code will tag each dist in neighbors_list with it's correct state

file_name = "helper-data/obsdist-stateID/obsdist-stateID.csv"
df_obsdist_stateID = pandas.read_csv(file_name)
# above dataframe have all meta of observed districts

obsdist_set = set()
for idx in df_obsdist_stateID.index:
    new_dist_name = df_obsdist_stateID.loc[idx, "state_id/dist_name_at_portal"]
    obsdist_set.add(new_dist_name)


obsdist_name_list = []
for dist in obsdist_set:
    temp = dist.split('/') # stateID/obsdist_name see above code block
    dist_name = temp[1]
    obsdist_name_list.append(dist_name)

file_name = "origdist-id/origdist-id.json"
file = open(file_name)
origdist_id_json = json.load(file)

origdist_list = []
for dist in origdist_id_json.keys():
    temp = dist.split('/')  # dist_name_modified_according to portal/Qid
    origdist_list.append(temp[0])
# print(origdist_list)

origdist_stateID_map = {}
for dist in origdist_id_json.keys():
    origdist_stateID_map[dist] = "*"

# imp part
for dist in origdist_id_json.keys():
    temp = dist.split('/')
    dist_name = temp[0]
    cnt = obsdist_name_list.count(dist_name)
    # print(dist, cnt)
    if cnt == 1:
        for idx in df_obsdist_stateID.index:
            if df_obsdist_stateID.loc[idx, "dist_name_at_portal"] == dist_name:
                origdist_stateID_map[dist] = df_obsdist_stateID.loc[idx, "state_id"]
                break
    
for dist in origdist_stateID_map.keys():
    if origdist_stateID_map[dist] == "*":
        if dist in dist_to_stateID.keys(): # reffer mapping python file
            origdist_stateID_map[dist] = dist_to_stateID[dist]

# a loop to test whether any origdist left for mapping from it's belonging state
# printed one is left one, it is a self helping code
# for dist in origdist_stateID_map.keys():
#     if origdist_stateID_map[dist] == "*":
#         print(dist)

path = "helper-data/origdist-stateID"
if not os.path.exists(path):
    os.mkdir(path)
file_name = os.path.join(path, "origdist-stateID.json")
with open(file_name, 'w') as fp_w :
    json.dump(origdist_stateID_map, fp_w, indent=4)

# print("Orig dist mapped with their state and saved at -> helper-data/origdist-stateID/origdist-stateID.json")
