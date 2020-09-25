#!/bin/sh

echo "started ..."

cd Code_and_Data

python3 top_hotspot_m.py > output1.txt
python3 top_hotspot_z.py > output2.txt

cp output1.txt ../
cp output2.txt ../

echo "finished ..."