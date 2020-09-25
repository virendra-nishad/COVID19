#!/usr/bin/env python3

import os
import csv
import json


parent_dir = os.getcwd()
path = parent_dir + "/origdist-id/origdist-id.json"
in_file = open(path)
origdist_id_json = json.load(in_file)

path = parent_dir + "/neighbor-districts-modified.json"
in_file = open(path)
nei_json = json.load(in_file)

with open('edge-graph.csv', mode='w') as out_file:
    fieldnames = ["dist-id", "adj-dist-id"]
    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)

    for dist in nei_json.keys():
        dist_id = origdist_id_json[dist]
        adj_dist_list = nei_json[dist]
        for adj_dist in adj_dist_list:
            adj_dist_id = origdist_id_json[adj_dist]
            out_writer.writerow([dist_id, adj_dist_id])

# print("edge-graph.csv -> created")