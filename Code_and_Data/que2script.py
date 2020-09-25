#!/usr/bin/env python3

import os
import json
import csv
import re
import pandas
import numpy
from mapping import correct_dist_map

data_path = "covid19data-json/data.json"
in_file = open(data_path)
origdata_json = json.load(in_file)

path = "origdist-id/origdist-id.json"
in_file = open(path)
origdist_id_json = json.load(in_file)


file_name = "helper-data/stateIDobsdist-origdistname/stateIDobsdist-origdistname.json"
in_file = open(file_name)
stateIDobsdist_origdistname_json = json.load(in_file)

origdist_case_count_template = {}

for dist in origdist_id_json.keys():
    origdist_case_count_template[dist] = 0
# print(origdist_casecount_template)

temp_case_count = origdist_case_count_template

with open('cases-week.csv', mode='w') as out_file:
    fieldnames = ["districtid", "week", "cases"]

    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)

    week_id = 0
    day_counter = 0
    for date in origdata_json.keys():
        # print(date)
        if date < '2020-03-15' or date > '2020-09-05':
            continue
        else:
            day_counter += 1
            for state in origdata_json[date].keys():
                if "districts" in origdata_json[date][state].keys():
                    dist_list = origdata_json[date][state]["districts"].keys()
                    for dist in dist_list:
                        new_dist_name = state + "/" + dist
                        if new_dist_name in stateIDobsdist_origdistname_json.keys():
                            origdist_mapped_name = stateIDobsdist_origdistname_json[new_dist_name]
                            if "delta" in origdata_json[date][state]["districts"][dist].keys():
                                if "confirmed" in origdata_json[date][state]["districts"][dist]["delta"].keys():
                                    temp_case_count[origdist_mapped_name] += origdata_json[date][state]["districts"][dist]["delta"]["confirmed"]
                
        if day_counter == 7:
            week_id += 1
            for dist in temp_case_count.keys():
                out_writer.writerow([origdist_id_json[dist], week_id, temp_case_count[dist]])
            day_counter = 0
            temp_case_count = dict.fromkeys(temp_case_count, 0)
            # print(temp_case_count)

# print("cases-week.csv -> created")

with open('cases-month.csv', mode='w') as out_file:
    fieldnames = ["districtid", "month", "cases"]

    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)

    month_id = 1
    month_str = "03"
    for date in origdata_json.keys():
        if date < '2020-03-15':
            continue
        else:
            for state in origdata_json[date].keys():
                if "districts" in origdata_json[date][state].keys():
                    dist_list = origdata_json[date][state]["districts"].keys()
                    for dist in dist_list:
                        new_dist_name = state + "/" + dist
                        if new_dist_name in stateIDobsdist_origdistname_json.keys():
                            origdist_mapped_name = stateIDobsdist_origdistname_json[new_dist_name]
                            if "delta" in origdata_json[date][state]["districts"][dist].keys():
                                if "confirmed" in origdata_json[date][state]["districts"][dist]["delta"].keys():
                                    temp_case_count[origdist_mapped_name] += origdata_json[date][state]["districts"][dist]["delta"]["confirmed"]
            
        month = date.split('-')
        if month[1] != month_str or date > "2020-09-05":
            for dist in temp_case_count.keys():
                out_writer.writerow([origdist_id_json[dist], month_id, temp_case_count[dist]])
            temp_case_count = dict.fromkeys(temp_case_count, 0)
            # print(temp_case_count)

            month_id += 1
            month_str = month[1]
            if date > "2020-09-05":
                break

# print("cases-month.csv -> created")


temp_case_count = dict.fromkeys(temp_case_count, 0)
with open('cases-overall.csv', mode='w') as out_file:
    fieldnames = ["districtid", "overall", "cases"]

    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)

    for date in origdata_json.keys():
        if date < '2020-03-15':
            continue
        else:
            for state in origdata_json[date].keys():
                if "districts" in origdata_json[date][state].keys():
                    dist_list = origdata_json[date][state]["districts"].keys()
                    for dist in dist_list:
                        new_dist_name = state + "/" + dist
                        if new_dist_name in stateIDobsdist_origdistname_json.keys():
                            origdist_mapped_name = stateIDobsdist_origdistname_json[new_dist_name]
                            if "delta" in origdata_json[date][state]["districts"][dist].keys():
                                if "confirmed" in origdata_json[date][state]["districts"][dist]["delta"].keys():
                                    temp_case_count[origdist_mapped_name] += origdata_json[date][state]["districts"][dist]["delta"]["confirmed"]

        if date > "2020-09-05":
            for dist in temp_case_count.keys():
                out_writer.writerow([origdist_id_json[dist], 1, temp_case_count[dist]])
            break

# print("cases-overall.csv -> created")