import pprint
import requests

while True:

    print('\n >>> Please enter the mac address: ')
    macInput = input()

    print('\n >>> Mac Address Vendor: ')

    MAC_URL = 'http://macvendors.co/api/%s'
    r = requests.get(MAC_URL % macInput)

    pprint.pprint(r.json())

    inp = input('\n >>> Would you like to check another mac address? (y/n): ')
    if(inp == "y" or inp == "Y"):
      continue
    else:
      print('\n See you soon!\n')
      break
