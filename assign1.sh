#!/bin/sh

echo "started ..."

cd Code_and_Data

python3 obsdist_stateID.py
python3 helper_for_mapping.py

python3 que1script.py

python3 map_origdist_with_stateID.py

python3 obsdist_origdist.py

python3 que2script.py

python3 que3script.py

python3 que4script.py

python3 que5script.py

python3 que6script.py

python3 que7script.py

python3 que8script.py

python3 top_hotspot_m.py > output1.txt
python3 top_hotspot_z.py > output2.txt

echo "Generating RESULTS ..."

cp neighbor-districts-modified.json ../
cp origdist-id/origdist-id.json ../

echo "Generating cases-time.csv ..."
cp cases-week.csv ../
cp cases-month.csv ../
cp cases-overall.csv ../

echo "Generating edeg-graph.csv ..."
cp edge-graph.csv ../

cp neighbor-week.csv ../
cp neighbor-month.csv ../
cp neighbor-overall.csv ../

echo "Generating state-time.csv ..."
cp state-week.csv ../
cp state-month.csv ../
cp state-overall.csv ../

echo "Generating zscore-time.csv ..."
cp zscore-week.csv ../
cp zscore-month.csv ../
cp zscore-overall.csv ../

echo "Generating method-spot-time.csv ..."
cp method-spot-week.csv ../
cp method-spot-month.csv ../
cp method-spot-overall.csv ../

echo "Generating top-time.csv ..."
cp top-week.csv ../
cp top-month.csv ../
cp top-overall.csv ../

echo "Generating output.txt ..."
cp output1.txt ../
cp output2.txt ../

echo "Finished ..."