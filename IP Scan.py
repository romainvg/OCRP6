import os
import time
import sys
from subprocess import Popen

devnull = open(os.devnull, 'wb')

print('====================================')

ip_subnet = input("Set the Subnet ( example: 192.168.0 ) --->")

print('====================================')

print('Scanning Subnet :\t' + ip_subnet)

print('====================================')

if ip_subnet == "":
    print('====================================')
    print("Please type a valid Subnet...")
    print('====================================')

p = []
active = 0
no_answer = 0
passive = 0

for interval in range(0, 255):
    ip = ip_subnet + ".%d" % interval
    p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None:
            p.remove((ip, proc))
            if proc.returncode == 0:
                print('%s active' % ip)
                active = active + 1
            elif proc.returncode == 2:
                print('%s No answer' % ip)
                active = no_answer + 1
            else:
                print('%s passive' % ip)
                passive = passive + 1
    time.sleep(.04)
devnull.close()

print('====================================')

print("LOCAL NETWORK IP SCANNER. COINPAIGN.")

print('====================================')

print('Current Operating System ' + os.name)
print("Network Status")
print("Active IP  [ ", active, " ]")
print("Passive IP [ ", passive, " ]")
print("No Answer  [ ", no_answer, " ]")

print('====================================')

scan_complete = "Scan Complete.."

print('= scan_complete')

print('====================================')
