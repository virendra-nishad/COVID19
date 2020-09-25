#!/bin/sh

echo "bar plot started ..."

cd Code_and_Data

python3 conclusion_number_of_hotspot.py
python3 conclusion_cases_count.py

cp -r plot-hotspot-count ../
cp -r plot-weekly-cases ../

echo "plots saved in folder plot-weekly-cases and plot-hotspot-count ..."
