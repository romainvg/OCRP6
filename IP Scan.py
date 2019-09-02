import sys
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

def main():

    arp()

main()
