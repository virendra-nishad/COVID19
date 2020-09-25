#!/usr/bin/env python3

import os
import json
import csv
import re
import pandas

####################################################################
# This will help in modifying given neighbor dist
# so that we can have uniform naming convention
####################################################################

parent_dir = os.getcwd()
dist_nei_path =  parent_dir + "/neighbor-districts/neighbor-districts.json"
in_file = open(dist_nei_path)
nei_dist_dict = json.load(in_file)

dist_in_nei_dist_list = sorted(nei_dist_dict.keys())

new_name_dict = {}
for dist in dist_in_nei_dist_list:
    temp = dist.split('/')
    dist_name = temp[0]
    dist_name = dist_name.lower()
    dist_name =  re.sub('[^0-9a-z]+', '_', dist_name)
    new_name = dist_name.replace("_district", "")
    new_name = new_name + '/' + temp[1]
    new_name_dict[dist] = new_name

new_neighbor_districts = {}
for dist in new_name_dict.keys():
    new_neighbor_districts[new_name_dict[dist]] = []
    nei_list = nei_dist_dict[dist]
    for nei_dist in nei_list:
        new_neighbor_districts[new_name_dict[dist]].append(new_name_dict[nei_dist])

path = parent_dir 
file_name = os.path.join(path, "neighbor-districts-temp.json")
with open(file_name, 'w') as fp_w :
    json.dump(new_neighbor_districts, fp_w, indent=4)

# print("temporary neighbor-districts-temp.json saved .")
# After this go to file => manual mapping