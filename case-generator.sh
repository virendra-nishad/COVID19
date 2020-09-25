#!/bin/sh

echo "started ..."

cd Code_and_Data

python3 obsdist_stateID.py
python3 helper_for_mapping.py

python3 que1script.py

python3 map_origdist_with_stateID.py

python3 obsdist_origdist.py

python3 que2script.py

cp cases-week.csv ../
cp cases-month.csv ../
cp cases-overall.csv ../

echo "Finished ..."