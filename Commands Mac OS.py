#################################################################################
#   The software is licensed Creative Commons CC-BY-NC-SA. Under this agreement #
#   you are authorized to use, share on the same rights or edit this software   #
#   for personnal purpose only. You are not allow to sell this software.        #
#                                                                               #
#    Official Website : https://coinpaign.com                                   #
#    Contact : romain.guihot@gmail.com                                          #

#   This file is not use by the remote administration yet, you can use it for   #
#   a command memento for Mac OSX                                               #
#################################################################################

# A SAVOIR :

            #  os.system() function permet l'execution de commande system
            #  subprocess.call() Function permet l'execution de commande system
            #  subprocess.call >= os.system ( + Rapide pour execute shell / bash commandes )

 ### IMPORTATIONS NECESSAIRES ###

import platform

## VOIR TYPE D'OS ##

osType = platform.system()
print("OS TYPE: " + osType)

## VOIR INFORMATIONS RESEAUX SIMPLIFIEES ##

import os

print("Voir Informations reseaux simplifiees :")
os.system("ifconfig |grep inet")

## VOIR INFORMATIONS RESEAUX DETAILLEES ##

import os

print("Voir Informations reseaux detaillees :")
os.system("ifconfig")

## VOIR ADDRESSE IP WAN ##

import os

print("Voir Addresse IP WAN / Public :")
os.system("curl ipecho.net/plain ; echo")

## VOIR LA TABLE DE ROUTAGE ##

import os

print("Voir la table de routage :")
os.system("netstat -nr")

## ETEINDRE LA MACHINE ##

import os
print("Eteindre la machine :")
os.system("sudo halt")

## REDEMARRER LA MACHINE ##

import os
print("Redemarrer la machine :")
os.system("reboot")

## FUN - MESSAGE VOCALE ##

import os
print("Entrer le message vocale :")
os.system("say hello world")
# Note : DEFINIR LE MESSAGE PAR FICHIER TXT : say -o audio.aiff -f FILENAME.txt

## VOIR LA VERSION DE L'OS ##

import os

print("Voir la version de l'OS :")
os.system("tail /System/Library/CoreServices/SystemVersion.plist | grep -A 1 ProductVersion")

## TELECHARGER UN FICHIER SANS NAVIGATEUR WEV ##

import os
print("Telecharger un fichier sans navigateur web :")
os.system("curl -0 *url_du_fichier_a_telecharger*")
# Note : curl -0 https://data-cdn.mbamupdates.com/web/mbam-mac-1.2.6.730.dmg

## EMPECHER TEMPORAIREMENT UN MAC DE SE METTRE EN VEILLE ##

import os
print("Empecher temporairement un Mac de se mettre en veille :")
os.system("caffeinate -u -t *nombre_de_secondes*")
# Note : caffeinate -u -99999999

## CONNAITRE TOUS LES PROCESSUS ACTIFS SUR UN ORDINATEUR APPLE ##

import os
print("Connaitre tous les processus actifs sur un ordinateur Apple :")
os.system("top")

## CONNAITRE UPTIME DE LA MACHINE ##

import os
print("Connaitre Uptime de la machine :")
os.system("uptime")


