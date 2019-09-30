#################################################################################
#                                                                               #
#  Mac_Vendor.py                                                                #
#                                                                               #
#  The software is licensed Creative Commons CC-BY-NC-SA. Under this agreement #
#  you are authorized to use, share on the same rights or edit this software   #
#  for personnal purpose only. You are not allow to sell this software.        #
#                                                                               #
#    Official Website : https://coinpaign.com                                   #
#    Contact : romain.guihot@gmail.com                                          #

#                                                                               #
#  This module is installed in Remote Administrator' computer.                  #
#  This is used in RemoteAdminTool.py.                                          #
#  Function:                                                                    #
#    1. Get vendor information corresponding to specified MAC                   #
#         information: address, company, country,                               # 
#                      end_hex, mac_prefix, start_hex, type                     # 
#                                                                               #
#################################################################################

import requests

def getMacVendor(mac):

    MAC_URL = 'http://macvendors.co/api/%s'
    
    r = requests.get(MAC_URL % mac)
    result = r.json()
    results = result["result"]
    
    return results
