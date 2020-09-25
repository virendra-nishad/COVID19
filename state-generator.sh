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

cp state-week.csv ../
cp state-month.csv ../
cp state-overall.csv ../

echo "finished ..."