#################################################################################
#                                                                               #
#  IP_Lookup.py                                                                 #
#                                                                               #
#  The software is licensed Creative Commons CC-BY-NC-SA. Under this agreement  #
#  you are authorized to use, share on the same rights or edit this software    #
#  for personnal purpose only. You are not allow to sell this software.         #
#                                                                               #
#  Official Website : https://coinpaign.com                                     #
#  Contact : romain.guihot@gmail.com                                            #           


#                                                                               #
#  This module is installed in Remote Administrator' computer.                  #
#  This is used in RemoteAdminTool.py.                                          #
#  Function:                                                                    #
#    1. Get IP address from domain address                                      #
#    2. Get some information of target IP' computer                             #
#        information:  country, city, region, location                          #
#                                                                               #
#################################################################################

import socket
import sys
import json
import requests

def func_getservip(target):

    try:
       s = socket.gethostbyname(target)
       getResult = "IP: " + str(s) + " | " + target 
    except:
       getResult = " Unknown Domain "
    
    return getResult

def func_whois(target):

    getResult = []
    output = requests.get('https://ipinfo.io/'+target+'/geo')
    content = output.text
    obj = json.loads(content)
    ss = str(obj).split(",")
    dd = ss[1].split("'")
    if dd[1] == "city":
      getResult.append(obj['ip'])
      getResult.append(obj['city'])
      getResult.append(obj['region'])
      getResult.append(obj['country'])
      getResult.append(obj['loc'])
      getResult.append(obj['readme'])
    else:
       getResult = []
    return getResult
