##########					              ##########
########## Commands Windows OS.py Feature ##########
##########						          ##########

#### LISTE DE COMMANDES WINDOWS OS ####

# A SAVOIR :

            #  os.system() function permet l'execution de commande system
            #  subprocess.call() Function permet l'execution de commande system
            #  subprocess.call >= os.system ( + Rapide pour execute shell / bash commandes )

 ### IMPORTATIONS NECESSAIRES ###

import platform

## VOIR TYPE D'OS ##

osType = platform.system()
print("OS TYPE: " + osType)

## VOIR TOUT LES PORTS ACTIFS ##

import os

print("Tout les ports actifs: ")
os.system("netstat -a")

## VOIR LES CONNEXIONS ENTRANTES/SORTANTES + PORTS ACTIFS##

import os

print("Liste des connexions entrantes/sortantes & ports actifs :")
os.system("netstat -n")

## VOIR FICHIERS EXECUTABLES A L'ORIGINE DES CONNEXIONS OU DES PORTS D'ECOUTE ##

import os
print("netstat -b")
os.system("netstat -b")
# Note : netstat -b -v 5 = Reactualiser toute les 5 secondes

## VOIR LES STATISTIQUES PAR PROTOCOLE ##

import os

print("Voir les statistiques par protocole:")
os.system("netstat -s")

## VOIR LA TABLE DE ROUTAGE ##

import os

print("Voir la table de routage:")
os.system("netstat -r")

## VOIR LE CHEMIN SUIVIT PAR UN PAQUET IP ##

import os

print("voir le chemin suivit par un paquet IP")
os.system("tracert 185.85.12.47")
# Note : IP A MODIFIER SELON LE SERVEUR SUIVI

## VOIR INFORMATIONS RESEAUX SIMPLIFIEES ##

import os

print("Information reseau simplifie")
os.system("ipconfig")

## VOIR INFORMATION IP PUBLIC DE LA MACHINE ##

import os
print("Voir IP public de la machine")
os.system("nslookup myip.opendns.com. resolver1.opendns.com")

## VOIR TOUTE LES INFORMATIONS RESEAUX DE LA MACHINE ##

import os

print("Informations reseaux detailles")
os.system("ipconfig /all")

## VOIR TOUTE LES @MAC DE TOUTE LES CARTES RESEAUX DE LA MACHINE ##

import os

print("Addresse mac des cartes reseaux")
os.system("getmac /v")

## EXECUTER UNE REQUETE PING ##

import os

print("Executer une requete ping")
os.system("ping 192.168.1.254")
# Note : DEFINIR L IP SELON LA REQUETE + FAIRE /t POUR REQUETE EN CONTINUE

## VOIR LES INFORMATIONS DE LA MACHINE ##

import os

print("Toute les informations de la machine")
os.system("systeminfo")

## ETEINDRE LA MACHINE ##

import os

print("Eteindre la machine")
os.system("shutdown")

## REDEMARRER LA MACHINE ##

import os

print("Redemarrer la machine")
os.system("shutdown -r")

## MONTRER LE REPERTOIRE BUREAU ##

import os

print("Acceder au bureau")
os.system("dir desktop")

## MONTRER LE REPERTOIRE DOCUMENT ##

import os

print("Acceder aux documents")
os.system("dir documents")

## MONTRER LE REPERTOIRE IMAGES ##

import os

print("Acceder aux images")
os.system("dir pictures")

## MONTRER LE REPERTOIRE TELECHARGEMENT ##

import os

print("Acceder aux telechargements")
os.system("dir downloads")

## MONTRER LES FICHIERS RECENTS ##

import os

print("Acceder au bureau")
os.system("dir recent")

## AFFICHIER TOUT LES PROCESSUS/SERVICES DE LA MACHINE ##

import os

print("Tout les processus en cours")
os.system("tasklist")

## AFFICHER LES SERVICES EN GUI ##

import os

print("Afficher les services actifs")
os.system("services.msc")

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

print("Afficher les peripheriques reseaux")
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

print("Gestionnaire des peripheriques")
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

print("Configurations des sessions de la machine")
os.system("netplwiz")

## AFFICHER LE REGISTRE DE LA MACHINE - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher le registre de la machine")
os.system("regedit")

## AFFICHER LES OPTIONS DE DEMARRAGES - ! GRAPHIQUE UNIQUEMENT ! ##

import os

print("Afficher les options de demarrages")
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

## FORCER LES GPO - ACTIVE DIRECTORY ##

import os
print("Forcer les GPO d'Active Directory")
os.system("gpupdate /force")

## CLAVIER VIRTUEL ##

import os
print("Afficher le clavier virtuel")
os.system("osk")







