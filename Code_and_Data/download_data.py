#!/usr/bin/env python3

import urllib.request
import json
import os

parent_dir = os.getcwd()

path = os.path.join(parent_dir, "covid19data-json")
if not os.path.exists(path):
    os.mkdir(path)

link = "https://api.covid19india.org/v4/data-all.json"

openUrl = urllib.request.urlopen(link)
if openUrl.getcode() == 200:
    data = openUrl.read()
    
    json_file_name = os.path.join(path, "data.json")
    with open(json_file_name, 'wb') as f:
        f.write(data)
else :
    print("error receiving data ", openUrl.getcode())
    
