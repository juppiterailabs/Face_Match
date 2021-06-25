import json 
import os

def read_config():
    DATA = {
        "REMOTE_ADDRS" : ["127.0.0.1"],
        "ALLOWED_EXTENTIONS" : ["png","jpg","jpeg"],
        "MAX_SIZE" : 5242880
        }
    conf_path = './config.json'
    if os.path.exists(conf_path):
        with open(conf_path,'r') as f:
            DATA = json.load(f)
    else:
        with open(conf_path,'w') as f:
            json.dump(DATA, f)
    return DATA

def save_config(data):
    conf_path = './config.json'
    with open(conf_path,'w') as f:
        json.dump(data, f)