# README

## How to run this project

    * This program is implemented sequentially, hence there might be dependence of one script on other.
    * There are sh script provided in root folder to run various modules individually without worrying about dependency.
    * There is also an script named "assign1.sh" which runs the entire program and create result as a text file named as output1.txt and output2.txt along with other output csv files needed. This output files are basically hot spot and cold spot as asked in question 7 and 8, but they contains name of district in place of id of districts.
    * assign1.sh should be run to save time as it will run entire project at once and generate all result.
    * All result files will be populated in root folder with name as said in assignment
    * Also there is a script named data_plot.sh which will plot bar plot of weekly cases of districts and also it will plot number of weekly hot spot for various method.

## Scripts

1. neighbor-districts-modifier.sh
    * It will create "neighbor-districts-modified.json" as well as it will also create a dictionary named "origdist-id.json" for mapping district with id starting from 101.

2. case-generator.sh
    * This script creates 3 csv files namely -
        * cases-week.csv
        * cases-month.csv
        * cases-overall.csv
    * All this files stores number of confirmed cases of each districts for duration like per week/month/overall

3. edge-generator.sh
    * This script generates an undirected graph of districts based on their adjacency with other districts and save this graph in a csv file named edge-graph.csv
    * This graph is generated after modification of given adjacent-districts.json and modification includes removal of districts if their record is not maintained at portal and merging adjacent districts of smaller districts to bigger one if removal of districts is initiated, removal of self loop in adjacency graph etc.

4. neighbor-generator.sh
    * This script generate 3 csv files -
        * neighbor-week.csv
        * neighbor-month.csv
        * neighbor-overall.csv
    * Each files contain mean and standard deviation of cases of neighboring districts. Identification of neighbor is as per neighbor-districts-modified.json

5. state-generator.sh
    * This script generates three csv files-
        * state-week.csv
        * state-month.csv
        * state-overall.csv
    * For every districts mean and standard deviations of all other districts in the same state is maintained by above csv files for different time duration.

6. zscore-generator.sh
    * This script generates 3 csv files-
        * zscore-week.csv
        * zscore-month.csv
        * zscore-overall.csv
    * Each files contains z score for each district based on neighboring districts as well as on the basis of other districts of the same state.

7. method-spot-generator.sh
    * This script generates 3 csv files-
        * method-spot-week.csv
        * method-spot-month.csv
        * method-spot-overall.csv
    * This script will find hot spots and cold spots by utilizing outputs of script neighbor-generator.sh and state-generator.sh

8. top-generator.sh
    * This script generates 3 csv files-
        * top-week.csv
        * top-month.csv
        * top-overall.csv
    * This script will generate hot spots and cold spots by utilizing z score generated by script zscore-generator.sh

9. top-hotspot-by-district-name.sh
    * This script is not asked in assignment.
    * Then main work of this script is to display hot spots by district name instead of district id.
    * This script will create two text file output1.txt and output2.txt
    * output1.txt contains hot spots based on mean and deviation
    * output2.txt contains hot spot based on z score
    * I used this script to draw conclusion as asked in question 10

10. data_plot.sh
    * This script is not asked in assignment.
    * I created this script to understand output by plotting bar plot and to draw conclusion for question 10.

## Results

    * All output files will be populated in root folder i.e where asked script are.

## Programming Language used

1. python3

## Libraries and modules used

    1. os
    2. csv
    3. json
    4. pandas
    5. numpy
    6. statistics
    7. re
    8. urllib.request
    9. matplotlib

## Data used

1. neighbor-districts.json
    * folder location: Code_and_Data/neighbor-districts
    * This data gives list of neighboring districts for the given district
2. data.json
    * folder location: Code_and_Data/covid19data-json
    * This json files keeps all info regarding COVID cases at district level

## Files in "Code_and_Data" folder

1. download_data.py

    * It is a python script to download COVID19 data from the portal given in assignment using below API
    * API: https://api.covid19india.org/v4/data-all.json
    * Data downloaded using above API has been saved in folder: Code_and_Data/covid19data-json
    * This downloaded json file maintain records of corona cases at district level.

2. obsdist_stateID.py
.
    * This script prepare a csv file which store meta related to observed districts which is needed in later part of program.
    * Generated CSV will be stored in folder helper-folder/obsdist_stateID

3. helper_for_mapping.py

    * There is spelling miss match between district names at portal and the district names provided in neighbors-districts.json.
    * To minimize error in name comparison of districts between two entries, this script create a third naming convention.
    * This naming convention has been used for implementation purpose only.

4. mapping.py

    * This file maintains a dictionary needed during implementation.

5. test_mapping.py

    * With the help of this script I was trying to figure out list of districts having miss match in names between district at portal and name of districts mentioned in neighbor-districts.json

6. que1script.py

    * This script is used to achieve the solution for Question 1
    * Output of this script is files:
        1. neighbor-districts-modified.json
            * It contains only those districts whose covid cases entries present at portal.
            * Districts present in this json file have name same as name of districts at portal.
            * Districts whose records are not present in portal are being merged with other adjacent districts, while merging district self loop have been removed and also neighbors of to be deleted districts have been made neighbors to new adjacent districts as asked in question
        2. origdist-id.json
            * This json file contains ID of districts present in new modified neighbors as mentioned in assignment.

7. map_origdist_with_stateID.py

    * This is a preprocessing script.
    * It's helps to map districts in neighbor-districts-modified.json to their corresponding state ID.
    * It's output is stored as: helper-data/origdist-stateID/origdist-stateID.json

8. obsdist_origdist.py

    * This is a preprocessing script.
    * It create a link between district at portal and district in neighbor-districts-modified.json in the form of creating a dictionary to map observed districts with new neighbors districts.

9. que2script.py
    * This script is used to create all those CSV asked in Question 2 and their output is stored as:
        1. cases-week.csv
        2. cases-month.csv
        3. cases-overall.csv

10. que3script.py
    * This script is used to create an undirected graph as asked in Question 3 and it's output is stored as:
        1. edge-graph.csv

11. que4script.py
    * This script is used to generate the solution for Question 4 and it's output is stored as files:
        1. neighbor-week.csv
        2. neighbor-month.csv
        3. neighbor-overall.csv

12. que5script.py
    * This script is used to generate solution for Question 5 and it's output is stored as files:
        1. state-week.csv
        2. state-month.csv
        3. state-overall.csv

13. que6script.py
    * This script is used to generate solution for Question 6 and it's output is stored as files:
        1. zscore-week.csv
        2. zscore-month.csv
        3. zscore-overall.csv

14. que7script.py
    * This script is used to generate solution for Question 7 and it's output is stored as files:
        1. method-spot-week.csv
        2. method-spot-month.csv
        3. method-spot-overall.csv

15. que8script.py
    * This script is used to generate solution for Question 8 and it's output is stored as files:
        1. top-month.csv
        2. top-overall.csv

16. top_hotspot_m.py
    * Although numbers are good for calculation but we are comfortable with name
    * This script generate hotspot district in term of district name not it's ID. It is not part of assignment, I have used it for understanding output.

17. top_hotspot_z.py
    * This script is again not part of assignment but I have implemented to understand output.
    * It's uses question 8 output and convert district id to name and also there is a variable named **number_of_dist** in the beginning of file que8script.py as well as top_hotspot_z.py to generate/display top n hotspot/coldspot districts. I used this because I wanted to see what are other districts which are also hotspots. So by setting value of this variable n number of hotspot can be generated.

18. conclusion_cases_count.py
    * It is a python script to plot bar plot for weekly confirmed cases.
    * I used this plot to see the trends in number of confirmed cases for each district

19. conclusion_number_of_hotspot.py
    * Plot a bar plot for number of hot spot per week.
    * Used this script to see whether the number of hot spot are increasing or decreasing.

Thanks you very much !
Virendra Nishad