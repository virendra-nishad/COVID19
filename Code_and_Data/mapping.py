#!/usr/bin/env python3

# this is manual mapping of all those district which was wrongly named by 
# person who was entering data
# need to import this module wherever needed


# few district in neighbour need to be merged
# 1. lakhimpur and kheri into lakhimpur_kheri
# 2. upper and lower dibang into dibang valley

import os
import json

correct_dist_map = {
    "airport_quarantine": "*",
    "aizawl": "aizwal",
    "amroha": "moradabad",
    "angul": "anugul",
    "ashoknagar": "ashok_nagar",
    "ayodhya": "faizabad",
    "bsf_camp": "*",
    "balasore": "baleshwar",
    "ballari": "bellary",
    "bametara": "bemetara",
    "banaskantha": "banas_kantha",
    "baramulla": "baramula",
    "beed": "bid",
    "belagavi": "belgaum",
    "bengaluru_rural": "bangalore_rural",
    "bengaluru_urban": "bangalore_urban",
    "bhadohi": "mirzapur",
    "boudh": "baudh",
    "budgam": "badgam",
    "chamarajanagara": "chamarajanagar",
    "chengalpattu": "chennai",
    "cooch_behar": "kochbihar",
    "dakshin_bastar_dantewada": "dantewada",
    "dang": "the_dangs",
    "dibang_valley" : "*",
    "delhi": "central_delhi",
    # "deogarh": "deoghar",
    "devbhumi_dwarka": "devbhumi_dwaraka",
    "dholpur": "dhaulpur",
    "east_champaran": "purba_champaran",
    "east_singhbhum": "purbi_singhbhum",
    "evacuees": "*",
    "fatehgarh_sahib": "fategarh_sahib",
    "ferozepur": "firozpur",
    "foreign_evacuees": "*",
    "ganganagar": "sri_ganganagar",
    "gaurela_pendra_marwahi": "bilaspur",
    "gondia": "gondiya",
    "hnahthial": "lunglei",
    "hooghly": "hugli",
    "italians": "*",
    "jagatsinghpur": "jagatsinghapur",
    "jajpur": "jajapur",
    "jalore": "jalor",
    #"jyotiba_phule_nagar" : "moradabad",
    "jhunjhunu" : "jhunjhunun",
    "kabeerdham": "kabirdham",
    "kaimur": "kaimur_bhabua_",
    "kalaburagi": "kalaburagi",
    "kancheepuram": "kanchipuram",
    "khawzawl": "lunglei",
    "koderma": "kodarma",
    "lahaul_and_spiti": "lahul_and_spiti",
    "lakhimpur_kheri" : "kheri",
    "maharajganj": "mahrajganj",
    "malda": "maldah",
    "mehsana": "mahesana",
    "mumbai": "konkan_division",
    
    "nandurbar": "nandubar",
    
    "narsinghpur": "narsimhapur",
    "navsari": "nav_sari",
    "nilgiris": "the_nilgiris",
    
    "other_region": "*",
    "other_state": "*",
    "others": "*",
    
    "pakur": "pakaur",
    "palakkad": "palghat",
    "panchmahal": "panch_mahal",
    "pathanamthitta": "pattanamtitta",
    
    "purulia": "puruliya",
    "rae_bareli": "rae_bareilly",
    
    "railway_quarantine": "*",
    "rajouri": "rajauri",
    "ranipet": "vellore",
    "ribhoi": "ri_bhoi",
    "s_a_s_nagar": "sahibzada_ajit_singh_nagar",
    "s_p_s_nellore": "sri_potti_sriramulu_nellore",
    "sabarkantha": "sabar_kantha",
    "saitual": "aizwal",
    
    
    "sant_kabir_nagar": "sait_kibir_nagar",
    "saraikela_kharsawan": "seraikela_kharsawan",
    "shahid_bhagat_singh_nagar": "shaheed_bhagat_singh_nagar",
    "shivamogga": "shimoga",
    "shopiyan": "shopian",
    "shrawasti": "sharawasti",
    "siddharthnagar": "siddharth_nagar",
    "sipahijala": "sepahijala",
    "sivaganga": "sivagangai",
    
    "sri_muktsar_sahib": "muktsar",

    "state_pool": "*",

    "subarnapur": "sonapur",
    
    "tenkasi": "tirunelveli_kattabo",
    
    "thoothukkudi": "thoothukudi",
    "tiruchirappalli": "tiruchchirappalli",
    "tirunelveli": "tirunelveli_kattabo",
    "tirupathur": "tiruppur",
    "tiruvannamalai": "tiruvanamalai",
    "tumakuru": "mysuru",
    
    "unknown": "*",

    "vijayapura": "bijapur",
    
    "west_champaran": "pashchim_champaran",
    
    "west_singhbhum": "pashchimi_singhbhum",
    "y_s_r_kadapa": "ysr",
    "yadgir": "yadagiri",
    "yanam": "*"
}

dist_to_stateID = {
    "Aurangabad/Q43086" : "BR",
    "Aurangabad/Q592942" : "MH",
    "Balrampur/Q16056268" : "CT",
    "Balrampur/Q1948380" : "UP",
    "Bilaspur/Q100157" : "CT",
    "Bilaspur/Q1478939" : "HP",
    "Hamirpur/Q2019757" : "UP",
    "Hamirpur/Q2086180" : "HP",
    "Pratapgarh/Q1473962" : "UP",
    "Pratapgarh/Q1585433" : "RJ"
}

# new_dict = {}

# key_dist = sorted(correct_dist_map.keys())
# print(key_dist)

# for dist in key_dist:
#     dist_name = correct_dist_map[dist]
#     new_name = dist_name.replace("_district", "")
#     new_dict[dist] = new_name

# parent_dir = os.getcwd()
# path = parent_dir + "/helper-data/manual-map/"
# if not os.path.exists(path):
#     os.mkdir(path)
# file_name = os.path.join(path, "manual-map.json")
# with open(file_name, 'w') as fp_w :
#     json.dump(new_dict, fp_w, indent=4)