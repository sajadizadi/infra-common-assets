#!/usr/bin/python

import yaml

def param(p):
    with open("config.yaml") as f_config:
        #load the files as yamls
        config = yaml.safe_load(f_config)
        print(config[p])