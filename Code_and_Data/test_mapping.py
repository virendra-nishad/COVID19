#!/usr/bin/env python3

import os
import json
import csv
import re
import pandas
from mapping import correct_dist_map

# helps in finding which observed dist has no map
# if any then manual prepare a dist map in manual map till all done

parent_dir = os.getcwd()
portal_dist_file_name = parent_dir + "/helper-data/obsdist-stateID/obsdist-stateID.csv"
df_portal_dist = pandas.read_csv(portal_dist_file_name)

observed_dist_name_list = list(df_portal_dist['dist_transformed_name'])

dist_nei_path =  parent_dir + "/neighbor-districts-temp.json"
in_file = open(dist_nei_path)
dict_nei_dist = json.load(in_file)

list_dist_in_nei_dist = sorted(dict_nei_dist.keys())

orig_dist_list = []
for dist in list_dist_in_nei_dist:
    temp = dist.split('/')
    orig_dist_list.append(temp[0])

dist_in_map_list = sorted(correct_dist_map.keys())

match_counter = 0
miss_match_counter = 0
miss_match_dist = []
dist_not_matched = []
for dist in observed_dist_name_list:
    if dist in orig_dist_list:
        match_counter += 1
    else:
        dist_not_matched.append(dist)
        if dist in dist_in_map_list:
            match_counter += 1
        else:
            miss_match_dist.append(dist)
            miss_match_counter += 1

print()
print()
print(miss_match_dist)
print(match_counter)
print(miss_match_counter)
print(dist_not_matched)
print(len(dist_not_matched))

# temp_dict = {}
# for dist in miss_match_dist:
#     temp_dict[dist] = "*"


# parent_dir = os.getcwd()
# path = parent_dir + "/helper_data/manual_orig_obs_map/"
# if not os.path.exists(path):
#     os.mkdir(path)
# file_name = os.path.join(path, "map_nei_orig.json")
# with open(file_name, 'w') as fp_w :
#     json.dump(temp_dict, fp_w, indent=4)


#####################################################################
# use output of this to create manual map of observed dist to orig dist