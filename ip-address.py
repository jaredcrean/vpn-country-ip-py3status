#!/bin/env python

import requests, json
class Py3status:
    
    # the ifconfig.co webpage ask that you only reload once every 60 sec.
    def __init__(self):
        self.url = 'http://ifconfig.co/json'


    def get_country(self):
        site = requests.get(url=self.url)
        get_json = json.loads(site.text)
        return get_json["country"]


    def get_ip(self):
        site = requests.get(url=self.url)
        get_json = json.loads(site.text)
        return get_json["ip"]
        #print(get_json["ip"])

    def country_ip(self):
        full_text  = "{} {} {}".format("VPN", self.get_country(), self.get_ip())
        return {
                'full_text': full_text,
        }
