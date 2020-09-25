#!/bin/sh

echo "started ..."

cd Code_and_Data

python3 obsdist_stateID.py
python3 helper_for_mapping.py

python3 que1script.py

cp neighbor-districts-modified.json ../
cp origdist-id/origdist-id.json ../

echo "finished ..."