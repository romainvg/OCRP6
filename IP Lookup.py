import socket
import os
import subprocess
import time
import sys
from datetime import datetime
from platform import system
from platform import version
import json
import requests
import urllib3
from urllib.request import urlopen


def main():

    print()
    print('++++++++++++++++++++++++++++++++++++')
    print('+ whois | Geolocate IP   +')
    print('+ getservip | Return Ip of Server +')
    print('+ exit  | Exit Script    +')
    print('++++++++++++++++++++++++++++++++++++')
    while True:
        choice = str(input('[$] Choice >'))

        if choice =='whois':
            print('[$] WELCOME TO THE IPLOOKUP')
            target = str(input('[$] Enter Target IP >'))
            output = requests.get('http://ipinfo.io/'+target+'/geo')
            content = output.text
            obj = json.loads(content)
            ip = obj['ip']
            city = obj['city']
            region = obj['region']
            country = obj['country']
            #hostname = obj['hostname']
            #name = obj['name']
            loc = obj['loc']
            postal = obj['postal']
            time.sleep(0.2)

            print('====================================')
            print('= IP : '+ip)
            print('= CITY : '+city)
            print('= REGION : '+region)
            print('= COUNTRY : '+country)
            print('= POSTAL : '+postal)
            #print('= HOSTNAME :'+hostname)
            #print('= NAME :'+name)
            print('= LOCATION : '+loc)
            print('===================================')

        if choice =='getservip':
            target =str(input('[$]) Enter the Target Website DOMAIN > '))

            s = socket.gethostbyname(target)
            print('IP : '+s+' | '+target)


        if choice =='exit':
            sys.exit('Exiting...')


main()
