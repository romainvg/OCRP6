#################################################################################
#                                                                               #
#  IP_Scan.py                                                                   #
#                                                                               #
#  This module is installed in Remote Administrator' computer.                  #
#  This is used in RemoteAdminTool.py.                                          #
#  Function:                                                                    #
#    1. Scan IP corresponding to specified subnet scope by using ARP            #
#                                                                               #
#################################################################################

import sys
from scapy.all import srp, Ether, ARP, conf

conf.verb = 0

def arp(ips):
    
    # ips = input("Enter Subnet & Subnet Mask ( Ex: 192.168.1.0/24) : ")

    print("\n[*] Scanning...")

    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ips), timeout=2)

    return ans

