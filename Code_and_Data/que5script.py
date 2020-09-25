#!/usr/bin/env python3

import json
import csv
import pandas
import statistics


file_name = "helper-data/origdist-stateID/origdist-stateID.json"
in_file = open(file_name)
origdist_stateID_json = json.load(in_file)
# print(origdist_stateID_json)

file_name = "origdist-id/origdist-id.json"
in_file = open(file_name)
origdist_id_json = json.load(in_file)
# print(origdist_id_json)


state_set = set()
for dist in origdist_stateID_json.keys():
    state_set.add(origdist_stateID_json[dist])
# print(state_set)

state_distlist_dict = {}
for state in state_set:
    state_distlist_dict[state] = []

for dist in origdist_stateID_json.keys():
    state_distlist_dict[origdist_stateID_json[dist]].append(origdist_id_json[dist])
# for state in state_distlist_dict.keys():
#     print(state, state_distlist_dict[state])

# just wanted to know which district lies in which state for fast calculation
# This information is required below
distID_stateID_dict = {}
for dist in origdist_id_json.keys():
    stateID = origdist_stateID_json[dist]
    distID_stateID_dict[origdist_id_json[dist]] = stateID
# print(distID_stateID_dict)






file_name = "cases-week.csv"
cases_week_df = pandas.read_csv(file_name)

# only one row with name cases, and many columns accessible as (districtid, week)
distIDtimeID_casecount_dict = cases_week_df.set_index(["districtid", "week"]).T.to_dict('list')

template_count = distIDtimeID_casecount_dict.copy()
for ki in template_count.keys():
    template_count[ki] = []
# for ki in template_count.keys():
#     print(ki, template_count[ki])


for ki in template_count.keys():
    distID = ki[0]
    state = distID_stateID_dict[distID]
    dist_in_state_list = state_distlist_dict[state]
    for dist in dist_in_state_list:
        # don't have to count own case count, thats why skipping 1 count
        if dist == distID:
            continue
        else:
            case_count = distIDtimeID_casecount_dict[(dist, ki[1])]
            template_count[ki].append(case_count[0])
# for ki in template_count.keys():
#     print(ki, template_count[ki])


out_df = cases_week_df.copy()

del out_df["cases"]

out_df["statemean"] = 0
out_df["statestdev"] = 0

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
                   
    out_df.loc[idx, "statemean"] = float("{:.2f}".format(mean))
    out_df.loc[idx, "statestdev"] = float("{:.2f}".format(std_dev))

# print(out_df)
out_df.to_csv("state-week.csv", index=False)
# print("state-week.csv -> created")






file_name = "cases-month.csv"
cases_month_df = pandas.read_csv(file_name)

# only one row with name cases, and many columns accessible as (districtid, week)
distIDtimeID_casecount_dict = cases_month_df.set_index(["districtid", "month"]).T.to_dict('list')

template_count = distIDtimeID_casecount_dict.copy()
for ki in template_count.keys():
    template_count[ki] = []
# for ki in template_count.keys():
#     print(ki, template_count[ki])

for ki in template_count.keys():
    distID = ki[0]
    state = distID_stateID_dict[distID]
    dist_in_state_list = state_distlist_dict[state]
    for dist in dist_in_state_list:
        if dist == distID:
            continue
        else:
            case_count = distIDtimeID_casecount_dict[(dist, ki[1])]
            template_count[ki].append(case_count[0])
# for ki in template_count.keys():
#     print(ki, template_count[ki])

out_df = cases_month_df.copy()

del out_df["cases"]

out_df["statemean"] = 0
out_df["statestdev"] = 0
# print(out_df)

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
            
            
    out_df.loc[idx, "statemean"] = float("{:.2f}".format(mean))
    out_df.loc[idx, "statestdev"] = float("{:.2f}".format(std_dev))

# print(out_df)
out_df.to_csv("state-month.csv", index=False)
# print("state-month.csv -> created")





file_name = "cases-overall.csv"
cases_overall_df = pandas.read_csv(file_name)

# only one row with name cases, and many columns accessible as (districtid, week)
distIDtimeID_casecount_dict = cases_overall_df.set_index(["districtid", "overall"]).T.to_dict('list')

template_count = distIDtimeID_casecount_dict.copy()
for ki in template_count.keys():
    template_count[ki] = []
# for ki in template_count.keys():
#     print(ki, template_count[ki])

for ki in template_count.keys():
    distID = ki[0]
    state = distID_stateID_dict[distID]
    dist_in_state_list = state_distlist_dict[state]
    for dist in dist_in_state_list:
        if dist == distID:
            continue
        else:
            case_count = distIDtimeID_casecount_dict[(dist, ki[1])]
            template_count[ki].append(case_count[0])
# for ki in template_count.keys():
#     print(ki, template_count[ki])

out_df = cases_overall_df.copy()

del out_df["cases"]

out_df["statemean"] = 0
out_df["statestdev"] = 0
# print(out_df)

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
            
    out_df.loc[idx, "statemean"] = float("{:.2f}".format(mean))
    out_df.loc[idx, "statestdev"] = float("{:.2f}".format(std_dev))

# print(out_df)
out_df.to_csv("state-overall.csv", index=False)
# print("state-overall.csv -> created")
