#!/usr/bin/env python3

import csv
import json
import pandas

number_of_dist = 5

# creating district string of the form districtid#
districts = []
for i in range(number_of_dist):
    districts.append("districtid" + str(i+1))

fieldnames = ["timeid", "method", "spot"]
for dist_id in districts:
    fieldnames.append(dist_id)

file_name = "zscore-week.csv"
zscore_week_df = pandas.read_csv(file_name)
# print(zscore_week_df)

with open('top-week.csv', mode='w') as out_file:

    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)

    
    for week_id in range(25):
        temp_cases_week_df = zscore_week_df.loc[zscore_week_df["week"] == week_id + 1]
        temp_cases_week_df = temp_cases_week_df.sort_values(by ='neighborhoodzscore', ascending=False )
        # print(temp_cases_week_df)
        dist_list = list(temp_cases_week_df["districtid"])

        data_row = [week_id+1, "neighborhood", "hotspot"]
        for i in range(number_of_dist):
            data_row.append(dist_list[i])
        out_writer.writerow(data_row)

        data_row = [week_id+1, "neighborhood", "coldspot"]
        for i in range(number_of_dist):
            data_row.append(dist_list[-(i+1)])
        out_writer.writerow(data_row)


        temp_cases_week_df = temp_cases_week_df.sort_values(by ='statezscore', ascending=False )
        # print(temp_cases_week_df)
        dist_list = list(temp_cases_week_df["districtid"])

        data_row = [week_id+1, "state", "hotspot"]
        for i in range(number_of_dist):
            data_row.append(dist_list[i])
        out_writer.writerow(data_row)

        data_row = [week_id+1, "state", "coldspot"]
        for i in range(number_of_dist):
            data_row.append(dist_list[-(i+1)])
        out_writer.writerow(data_row)
# print("top-week.csv -> created")




file_name = "zscore-month.csv"
zscore_month_df = pandas.read_csv(file_name)

with open('top-month.csv', mode='w') as out_file:

    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)

    
    for month_id in range(7):
        temp_cases_month_df = zscore_month_df.loc[zscore_month_df["month"] == month_id + 1]
        temp_cases_month_df = temp_cases_month_df.sort_values(by ='neighborhoodzscore', ascending=False )
        # print(temp_cases_week_df)
        dist_list = list(temp_cases_month_df["districtid"])

        data_row = [month_id+1, "neighborhood", "hotspot"]
        for i in range(number_of_dist):
            data_row.append(dist_list[i])
        out_writer.writerow(data_row)

        data_row = [month_id+1, "neighborhood", "coldspot"]
        for i in range(number_of_dist):
            data_row.append(dist_list[-(i+1)])
        out_writer.writerow(data_row)


        temp_cases_month_df = temp_cases_month_df.sort_values(by ='statezscore', ascending=False )
        # print(temp_cases_week_df)
        dist_list = list(temp_cases_month_df["districtid"])

        data_row = [month_id+1, "state", "hotspot"]
        for i in range(number_of_dist):
            data_row.append(dist_list[i])
        out_writer.writerow(data_row)

        data_row = [month_id+1, "state", "coldspot"]
        for i in range(number_of_dist):
            data_row.append(dist_list[-(i+1)])
        out_writer.writerow(data_row)
# print("top-month.csv -> created")



file_name = "zscore-overall.csv"
zscore_overall_df = pandas.read_csv(file_name)
# print(zscore_overall_df)

with open('top-overall.csv', mode='w') as out_file:

    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(fieldnames)
    
    # temp_cases_overall_df = zscore_overall_df.loc[zscore_month_df["over"] == month_id + 1]
    temp_cases_overall_df = zscore_overall_df.sort_values(by ='neighborhoodzscore', ascending=False )
    # print(temp_cases_overall_df)
    dist_list = list(temp_cases_overall_df["districtid"])

    data_row = [1, "neighborhood", "hotspot"]
    for i in range(number_of_dist):
        data_row.append(dist_list[i])
    out_writer.writerow(data_row)

    data_row = [1, "neighborhood", "coldspot"]
    for i in range(number_of_dist):
        data_row.append(dist_list[-(i+1)])
    out_writer.writerow(data_row)


    temp_cases_overall_df = zscore_overall_df.sort_values(by ='statezscore', ascending=False )
    # print(temp_cases_overall_df)
    dist_list = list(temp_cases_overall_df["districtid"])

    data_row = [1, "state", "hotspot"]
    for i in range(number_of_dist):
        data_row.append(dist_list[i])
    out_writer.writerow(data_row)

    data_row = [1, "state", "coldspot"]
    for i in range(number_of_dist):
        data_row.append(dist_list[-(i+1)])
    out_writer.writerow(data_row)
# print("top-overall.csv -> created")