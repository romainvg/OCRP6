##########					             ##########
########## Commands Linux OS.py Feature  ##########
##########						         ##########

#### LISTE DE COMMANDES WINDOWS OS ####

# A SAVOIR :

            #  os.system() function permet l'execution de commande system
            #  subprocess.call() Function permet l'execution de commande system
            #  subprocess.call >= os.system ( + Rapide pour execute shell / bash commandes )

 ### IMPORTATIONS NECESSAIRES ###

import platform

osType = platform.system()
print("OS TYPE: " + osType)

## VOIR TOUT LES PORTS EN ECOUTE ##

import os

print("Tout les ports en ecoute: ")
os.system("netstat -laputen | grep LISTEN")


## VOIR TOUTES LES CONNEXIONS ENTRANTES/SORTANTES + PORT ACTIFS ##

import os

print("Toutes les connexions entrantes / sortantes & ports actifs: ")
os.system("netstat -paunt")

## VOIR LES STATISTIQUES PAR PROTOCOLE ##

import os

print("Voir les statistiques par protocole:")
os.system("netstat -s")

## VOIR QUEL PORT EST UTILISE PAR UN PROGRAMME ( Optionnel ) ##

import os
print("Voir quel port est utilise par un programme")
os.system("netstat -ap | grep ssh")

## VOIR QUEL PROCESSUS UTILISE UN PORT PARTCULIER ( Optionnel ##

import os
print("voir quel processus utilise un port particulier")
os.system("netstat -an | grep ':80'")

## VOIR LA TABLE DE ROUTAGE ##

import os

print("Voir la table de routage:")
os.system("route -n")

## VOIR LE CHEMIN SUIVIT PAR UN PAQUET IP ##

import os

print("voir me chemin suivit par un paquet IP")
os.system("traceroute 185.85.12.47")
# Note : IP A MODIFIER SELON LE SERVEUR SUIVIT

## VOIR INFORMATION RESEAU SIMPLIFIE ##

import os

print("Voir Informations reseaux:")
os.system("ifconfig")

## OBTENIR UNIQUEMENT L'ADDRESSE IP ##

import os

print("Obtenir uniquement @IP:")
os.system("hostname -I")

## EXECUTER UNE REQUETE PING ##

import os

print("Executer une requete ping:")
os.system("ping 192.168.1.254")
# Note : Definir L'IP en fonction des besoins

## VOIR TOUTE LES @MAC DE TOUTE LES CARTES RESEAUX DE LA MACHINE ##

import os

print("Addrese mac des cartes reseaux:")
os.system("ip link")

## VOIR LES INFORMATIONS DU SYSTEME D'EXPLOITATION ##

import os

print("Afficher les Informations OS:")
os.system("uname -a")

## VOIR LES INFORMATIONS RAM DE LA MACHINE ##

import os

print("Afficher les informations RAM:")
os.system("cat /proc/meminfo")

## VOIR LES INFORMATIONS PROCESSEUR DE LA MACHINE ##

import os

print("Afficher les informations processeur:")
os.system("cat /proc/cpuinfo")

## MODIFICATION DES CARTES RESEAUX ##

import os
print("Modification cartes reseaux:")
os.system("nano /etc/network/interfaces")

## MODIFICATION RESOLUTION DE NOM = DNS ##

import os
print("Modification resolution de nom:")
os.system ("nano /etc/resolv.conf")

## REDEMARRER LES CARTES RESEAUX ##

import os
print ("Redemarrer les cartes reseaux:")
os.system("/etc/init.d/networking restart")

## VOIR INFORMATION NOM DE DOMAINE ##

import os
print("Voir information du domaine / IP")
os.system("nslookup google.fr")
# Note : nom de domaine ou IP

## ETEINDRE LA MACHINE ##

import os
print("Eteindre la machine")
os.system("shutdown now")

## REDEMARRER LA MACHINE ##

import os
print("Redemarrer la machine")
os.system("reboot")