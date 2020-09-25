#!/usr/bin/env python3

import csv
import json
import pandas
import statistics

# temp_case_count = dict.fromkeys(temp_case_count, 0)

file_name = "neighbor-districts-modified.json"
in_file = open(file_name)

neighbor_json = json.load(in_file)
# print(nei_dist_name_json)

file_name = "origdist-id/origdist-id.json"
in_file = open(file_name)
origdist_id_json = json.load(in_file)

# store neigbour info in form dist id only instead of ugly name
nei_dist_id_dict = {}
for dist in neighbor_json.keys():
    nei_dist_id_dict[origdist_id_json[dist]] = []
    for adj_dist in neighbor_json[dist]:
        nei_dist_id_dict[origdist_id_json[dist]].append(origdist_id_json[adj_dist])



file_name = "cases-week.csv"
cases_week_df = pandas.read_csv(file_name)

# only one row with name cases, and many columns accessible as (districtid, week)
distIDtimeID_casecount_dict = cases_week_df.set_index(["districtid", "week"]).T.to_dict('list')

template_count = distIDtimeID_casecount_dict.copy()
# template_count = dict.fromkeys(template_count, 0)

for ki in template_count.keys():
    template_count[ki] = []
# for ki in template_count.keys():
#     print(ki, template_count[ki])

for ki in template_count.keys():
    adj_dist_id = nei_dist_id_dict[ki[0]]
    for dist in adj_dist_id:
        case_count = distIDtimeID_casecount_dict[(dist, ki[1])]
        template_count[ki].append(case_count[0])
# for ki in template_count.keys():
#     print(ki, template_count[ki])

out_df = cases_week_df.copy()

del out_df["cases"]

out_df["neighbormean"] = 0
out_df["neighborstdev"] = 0

for idx in out_df.index:
    ki = (out_df.loc[idx, "districtid"], out_df.loc[idx, "week"])
    nei_cases_count_list = template_count[ki]
    mean = 0
    std_dev = 0
    if len(nei_cases_count_list) > 1:
        mean = statistics.mean(nei_cases_count_list)
        std_dev = statistics.stdev(nei_cases_count_list)
    else:
        if len(nei_cases_count_list) == 1:
            mean = nei_cases_count_list[0]
            std_dev = 0
        
    out_df.loc[idx, "neighbormean"] = float("{:.2f}".format(mean))
    out_df.loc[idx, "neighborstdev"] = float("{:.2f}".format(std_dev))
    # print(nei_cases_count_list)

# print(out_df)
out_df.to_csv("neighbor-week.csv", index=False)
# print("neighbor-week.csv -> created")




file_name = "cases-month.csv"
cases_month_df = pandas.read_csv(file_name)

distIDtimeID_casecount_dict = cases_month_df.set_index(["districtid", "month"]).T.to_dict('list')

template_count = distIDtimeID_casecount_dict.copy()
for ki in template_count.keys():
    template_count[ki] = []
# for ki in template_count.keys():
#     print(ki, template_count[ki])

for ki in template_count.keys():
    adj_dist_id = nei_dist_id_dict[ki[0]]
    for dist in adj_dist_id:
        case_count = distIDtimeID_casecount_dict[(dist, ki[1])]
        template_count[ki].append(case_count[0])
# for ki in template_count.keys():
#     print(ki, template_count[ki])

out_df = cases_month_df.copy()

del out_df["cases"]

out_df["neighbormean"] = 0
out_df["neighborstdev"] = 0

for idx in out_df.index:
    ki = (out_df.loc[idx, "districtid"], out_df.loc[idx, "month"])
    nei_cases_count_list = template_count[ki]
    mean = 0
    std_dev = 0
    if len(nei_cases_count_list) > 1:
        mean = statistics.mean(nei_cases_count_list)
        std_dev = statistics.stdev(nei_cases_count_list)
    else:
        if len(nei_cases_count_list) == 1:
            mean = nei_cases_count_list[0]
            std_dev = 0
               
    out_df.loc[idx, "neighbormean"] = float("{:.2f}".format(mean))
    out_df.loc[idx, "neighborstdev"] = float("{:.2f}".format(std_dev))

# print(out_df)
out_df.to_csv("neighbor-month.csv", index=False)
# print("neighbor-month.csv -> created")




file_name = "cases-overall.csv"
cases_overall_df = pandas.read_csv(file_name)

distIDtimeID_casecount_dict = cases_overall_df.set_index(["districtid", "overall"]).T.to_dict('list')

template_count = distIDtimeID_casecount_dict.copy()
for ki in template_count.keys():
    template_count[ki] = []
# for ki in template_count.keys():
#     print(ki, template_count[ki])

for ki in template_count.keys():
    adj_dist_id = nei_dist_id_dict[ki[0]]
    for dist in adj_dist_id:
        case_count = distIDtimeID_casecount_dict[(dist, ki[1])]
        template_count[ki].append(case_count[0])
# for ki in template_count.keys():
#     print(ki, template_count[ki])

out_df = cases_overall_df.copy()

del out_df["cases"]

out_df["neighbormean"] = 0
out_df["neighborstdev"] = 0

for idx in out_df.index:
    ki = (out_df.loc[idx, "districtid"], out_df.loc[idx, "overall"])
    nei_cases_count_list = template_count[ki]
    mean = 0
    std_dev = 0
    if len(nei_cases_count_list) > 1:
        mean = statistics.mean(nei_cases_count_list)
        std_dev = statistics.stdev(nei_cases_count_list)
    else:
        if len(nei_cases_count_list) == 1:
            mean = nei_cases_count_list[0]
            std_dev = 0
            
    out_df.loc[idx, "neighbormean"] = float("{:.2f}".format(mean))
    out_df.loc[idx, "neighborstdev"] = float("{:.2f}".format(std_dev))

# print(out_df)
out_df.to_csv("neighbor-overall.csv", index=False)
# print("neighbor-overall.csv -> created")