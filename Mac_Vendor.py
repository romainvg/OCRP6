#################################################################################
#                                                                               #
#  Mac_Vendor.py                                                                #
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