#!/usr/bin/env python3

import json
import csv
import pandas
import matplotlib.pyplot as plt
import os

file_name = "origdist-id/origdist-id.json"
in_file = open(file_name)
origdist_id_json = json.load(in_file)

id_distname_dict = {}
for dist in origdist_id_json.keys():
    dist_name = dist.split('/')
    id_distname_dict[origdist_id_json[dist]] = dist_name[0]


filename = "cases-week.csv"
df = pandas.read_csv(filename)
for dist_id in range(101,718):
    print(id_distname_dict[dist_id])
    temp_df = df[(df["districtid"] == dist_id)]

    # print(temp_df)

    # cases_count = list(temp_df["cases"])
    fig = plt.bar(temp_df["week"], temp_df["cases"])
    plt.title(id_distname_dict[dist_id])
    plt.ylabel("case count")
    plt.xlabel("week number")

    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, "plot-weekly-cases")
    # path = parent_dir "plot/case_count/"
    if not os.path.exists(path):
        os.mkdir(path)
    fig_name = id_distname_dict[dist_id] + ".png"
    plt.savefig(os.path.join(path, fig_name))
    plt.clf()

