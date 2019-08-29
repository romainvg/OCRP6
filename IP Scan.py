import sys
import os
import os.path
from datetime import datetime
from scapy.all import srp, Ether, ARP, conf

conf.verb = 0


def arp():
    try:
        ips = input("Enter Subnet & Subnet Mask ( Ex: 192.168.1.0/24) : ")

    except KeyboardInterrupt:
        print("\n[*] User Requested Shutdown")
        print("[*] Quitting...")
        sys.exit(1)

    print("\n[*] Scanning...")
    start_time = datetime.now()
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ips), timeout=2)

    print("MAC - IP\n")
    for snd, rcv in ans:
        print(rcv.sprintf(r"%Ether.src% - %ARP.psrc%"))
    stop_time = datetime.now()
    total_time = stop_time - start_time
    print("\n[*] Scan Complete!")
    print("[*] Scan Duration: %s" % (total_time))

    devices = {}
    for snd, rcv in ans:
        print(rcv.psrc + "\t\t" + rcv.src)
        devices[rcv.src] = rcv.psrc

    return devices


def createText(deviceList):
    devices = open("devices.txt", "w")
    for mac, ip in deviceList.iteritems():
        devices.write(mac + "&" + ip + "\n")
    devices.close()


def textList():
    l = open("devices.txt", "r")
    List = l.readlines()
    textList = {}
    for i in range(len(List)):
        mac, ip = List[i].split("&")
        ip = ip[:-1]
        textList[mac] = ip

    l.close()
    return textList


def checkText():
    newText = {}
    oldText = {}
    newText = arp()
    oldText = textList()
    lastMacs = list(oldText.keys())
    newMacs = list(newText.keys())
    text = {}

    for i in range(len(newText)):
        if newMacs[i] in lastMacs:
            if (newText[newMacs[i]] == oldText[newMacs[i]]):
                text[newMacs[i]] = newText[newMacs[i]]
                continue
            else:
                while (1):
                    option = input("\n[*] IP of The MAC address %s that is in your lan has changed. Do you want save this change ? (y/n): " %newMacs[i])
                    if (option == "y" or option == "Y"):
                        text[newMacs[i]] = newText[newMacs[i]]
                        break
                    elif (option == "n" or option == "N"):
                        text[newMacs[i]] = oldText[newMacs[i]]
                        break
                    else:
                        print('[*] Please Only Select "Y" or "N" Option!')
        else:
            while (1):
                option = input("\n[*] Do you want save this device: %s to list ? (y/n): " % newMacs[i])
                if (option == "y" or option == "Y"):
                    text[newMacs[i]] = newText[newMacs[i]]
                    break
                elif (option == "n" or option == "N"):
                    break
                else:
                    print('[*] Please Select Only "Y" or "N" Option !')
    createText(text)


def main():
    if os.path.exists("devices.txt"):
        checkText()
    else:
        createText(arp())


main()