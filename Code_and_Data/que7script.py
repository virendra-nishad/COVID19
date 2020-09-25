#!/usr/bin/env python3

import csv
import json
import pandas

file_name = "cases-week.csv"
cases_week_df = pandas.read_csv(file_name)
# print(cases_week_df)

file_name = "neighbor-week.csv"
neighbor_week_df = pandas.read_csv(file_name)
neighbor_week_df = neighbor_week_df.set_index(["districtid", "week"])
# print(neighbor_week_df)

file_name = "state-week.csv"
state_week_df = pandas.read_csv(file_name)
state_week_df = state_week_df.set_index(["districtid", "week"])
# print(state_week_df)


with open('method-spot-week.csv', mode='w') as out_file:

    fieldnames = ["timeid", "method", "spot", "districtid"]

    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)

    for idx in cases_week_df.index:
        week = cases_week_df.loc[idx, "week"]
        distid = cases_week_df.loc[idx, "districtid"]
        case = cases_week_df.loc[idx, "cases"]     # cases is xi

        nei_mean = neighbor_week_df.loc[(distid, week), "neighbormean"]
        nei_stdev = neighbor_week_df.loc[(distid, week), "neighborstdev"]

        state_mean = state_week_df.loc[(distid, week), "statemean"]
        state_stdev = state_week_df.loc[(distid, week), "statestdev"]

        nei_upper_bound = nei_mean + nei_stdev
        nei_lower_bound = nei_mean - nei_stdev

        state_upper_bound = state_mean + state_stdev
        state_lower_bound = state_mean - state_stdev

        if case > nei_upper_bound:
            timeid = week
            method = "neighborhood"
            spot = "hotspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])
        if case < nei_lower_bound:
            timeid = week
            method = "neighborhood"
            spot = "coldspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])

        if case > state_upper_bound:
            timeid = week
            method = "state"
            spot = "hotspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])
        if case < state_lower_bound:
            timeid = week
            method = "state"
            spot = "coldspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])
# print("method-spot-week.csv -> created")






file_name = "cases-month.csv"
cases_month_df = pandas.read_csv(file_name)
# print(cases_month_df)

file_name = "neighbor-month.csv"
neighbor_month_df = pandas.read_csv(file_name)
neighbor_month_df = neighbor_month_df.set_index(["districtid", "month"])
# print(neighbor_month_df)

file_name = "state-month.csv"
state_month_df = pandas.read_csv(file_name)
state_month_df = state_month_df.set_index(["districtid", "month"])
# print(state_month_df)

with open('method-spot-month.csv', mode='w') as out_file:

    fieldnames = ["timeid", "method", "spot", "districtid"]

    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)

    for idx in cases_month_df.index:
        month = cases_month_df.loc[idx, "month"]
        distid = cases_month_df.loc[idx, "districtid"]
        case = cases_month_df.loc[idx, "cases"]     # cases is xi

        nei_mean = neighbor_month_df.loc[(distid, month), "neighbormean"]
        nei_stdev = neighbor_month_df.loc[(distid, month), "neighborstdev"]

        state_mean = state_month_df.loc[(distid, month), "statemean"]
        state_stdev = state_month_df.loc[(distid, month), "statestdev"]

        nei_upper_bound = nei_mean + nei_stdev
        nei_lower_bound = nei_mean - nei_stdev

        state_upper_bound = state_mean + state_stdev
        state_lower_bound = state_mean - state_stdev

        if case > nei_upper_bound:
            timeid = month
            method = "neighborhood"
            spot = "hotspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])
        if case < nei_lower_bound:
            timeid = month
            method = "neighborhood"
            spot = "coldspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])

        if case > state_upper_bound:
            timeid = month
            method = "state"
            spot = "hotspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])
        if case < state_lower_bound:
            timeid = month
            method = "state"
            spot = "coldspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])
# print("method-spot-month.csv -> created")





file_name = "cases-overall.csv"
cases_overall_df = pandas.read_csv(file_name)
# print(cases_overall_df)

file_name = "neighbor-overall.csv"
neighbor_overall_df = pandas.read_csv(file_name)
neighbor_overall_df = neighbor_overall_df.set_index(["districtid", "overall"])
# print(neighbor_overall_df)

file_name = "state-overall.csv"
state_overall_df = pandas.read_csv(file_name)
state_overall_df = state_overall_df.set_index(["districtid", "overall"])
# print(state_overall_df)

with open('method-spot-overall.csv', mode='w') as out_file:

    fieldnames = ["timeid", "method", "spot", "districtid"]

    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)

    for idx in cases_overall_df.index:
        overall = cases_overall_df.loc[idx, "overall"]
        distid = cases_overall_df.loc[idx, "districtid"]
        case = cases_overall_df.loc[idx, "cases"]     # cases is xi

        nei_mean = neighbor_overall_df.loc[(distid, overall), "neighbormean"]
        nei_stdev = neighbor_overall_df.loc[(distid, overall), "neighborstdev"]

        state_mean = state_overall_df.loc[(distid, overall), "statemean"]
        state_stdev = state_overall_df.loc[(distid, overall), "statestdev"]

        nei_upper_bound = nei_mean + nei_stdev
        nei_lower_bound = nei_mean - nei_stdev

        state_upper_bound = state_mean + state_stdev
        state_lower_bound = state_mean - state_stdev

        if case > nei_upper_bound:
            timeid = overall
            method = "neighborhood"
            spot = "hotspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])
        if case < nei_lower_bound:
            timeid = overall
            method = "neighborhood"
            spot = "coldspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])

        if case > state_upper_bound:
            timeid = overall
            method = "state"
            spot = "hotspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])
        if case < state_lower_bound:
            timeid = overall
            method = "state"
            spot = "coldspot"
            districtid = distid
            out_writer.writerow([timeid, method, spot, districtid])
# print("method-spot-overall.csv -> created")               