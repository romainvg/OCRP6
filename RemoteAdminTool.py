####################################################################################
#                                                                                  #
#  RemoteAdminTool.py                                                              #
#                                                                                  #                                                                            #
#  The software is licensed Creative Commons CC-BY-NC-SA. Under this agreement     #
#  you are authorized to use, share on the same rights or edit this software       #
#  for personnal purpose only. You are not allow to sell this software.            #
#                                                                                  #
#    Official Website : https://coinpaign.com                                      #
#    Contact : romain.guihot@gmail.com                                             #
                                                                               
#  This module is installed in Remote Administrator' computer.                     #
#  This is main program for remote administration tool used in Coinpaign           #
#  management environment(local area network).                                     #
#    ps: CME-Coinpaign Management Environment                                      #
#  Function:                                                                       #
#     1. Administration tool GUI                                                   #
#     2. Get and display various information of computers in CME                   #
#     3. Provide various network tools                                             #
#          tools: IP_Scan, Port_Scan, IP_Lookup, Mac_Vendor                        #
#     4. Reverse shell to control remote computers in CME                          #
#     5. Remote Desktop Connection in CME                                          #
#                                                                                  #
####################################################################################

#--- standard package
import sys
import time
import socket
import json
import platform
import subprocess
from subprocess import Popen

#--- dependent package
import qdarkstyle
import netifaces
import pycountry
from urllib.request import urlopen

from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QStandardItemModel, QIcon, QStandardItem, QPixmap, QCursor, QRegExpValidator
from PyQt5.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit, QTreeView, QVBoxLayout, QDialog,
 QWidget, QMenu, QPushButton, QMessageBox, QAction, QSplashScreen, QProgressBar, QTextEdit)

#--- developed sub module 
import AgentClient
import IP_Scan
import Port_Scan
import IP_Lookup
import Mac_Vendor

serverdata = []   #--- global variable for data of remote computer

class App(QWidget):
    
    Country, IPAddress, SessionName, Status, OS,  CPU, CPU_Core, RAM, PING = range(0, 9)
    
    def __init__(self):
        
        super().__init__()
        
#=========== Main GUI block ==================        
      # Main Window Setting
        self.title = 'COINPAIGN: Remote Administration Tool'
        self.setWindowIcon(QIcon('logo.ico'))
        self.left = 500
        self.top = 250
        self.width = 1000
        self.height = 500

      # Getting subnet, LAN and WAN
        host = self.get_Host_name_IP() 
        self.local = host[0]
        self.subnet_mask = host[1]

        self.initUI()
        self.displayItem()

    def initUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.dataGroupBox = QGroupBox()
        self.dataView = QTreeView()
        # self.dataView.move(0,100)
        # self.dataView.resize(500, 500)

        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)
        self.dataView.setSortingEnabled(True)
        
        dataLayout = QVBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)
                
        self.dataView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.dataView.customContextMenuRequested.connect(self.openMenu)

    # Layout "Refresh" button
        button = QPushButton('Refresh', self)
        button.move(900,5)
        button.resize(80, 20)
        button.clicked.connect(self.execute_Refresh)
        
    # Layout "IP Lookup" button
        button = QPushButton('IP Lookup', self)
        button.move(15,5)
        button.resize(80, 20)
        button.clicked.connect(self.execute_IPlookup)
    
    # Layout "MAC Vendor" button
        button = QPushButton('MAC Vendor', self)
        button.move(110,5)
        button.resize(80, 20)
        button.clicked.connect(self.execute_MACvendor)

    def createMailModel(self,parent = None):  #--- create information table view of remote computer
        
        model = QStandardItemModel(0, 9, parent)
        
        model.setHeaderData(self.Country, Qt.Horizontal, "Country/City ")
        model.setHeaderData(self.IPAddress, Qt.Horizontal, "IP LAN/WAN")
        model.setHeaderData(self.SessionName, Qt.Horizontal, "SessionName")
        model.setHeaderData(self.Status, Qt.Horizontal, "Status")
        model.setHeaderData(self.OS, Qt.Horizontal, "OS")
        model.setHeaderData(self.CPU, Qt.Horizontal, "CPU")
        model.setHeaderData(self.CPU_Core, Qt.Horizontal, "CPU Core")
        model.setHeaderData(self.RAM, Qt.Horizontal, "RAM(GB)")
        model.setHeaderData(self.PING, Qt.Horizontal, "PING(ms)")
                
        return model

#=========== Get and dislay information of remote computers block ==================            
    def displayItem(self):      #--- get and display information of remote computer when applictoin start
        
        progressBar.setMaximum(254)

        #--- get information of remote computer
        for i in range(1, 254):
            host = self.subnet_mask + ".%d" % i
            data = AgentClient.client_program(host)  #--- get data from Agentclient module
                     
            if data != "0":
                pi = self.get_pingtime(host)
                data = data+":"+str(pi)
                serverdata.append(data)
            
            progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                app.processEvents()
        
        #--- display information of remote computer
        self.onReload()       
        
        splash.hide()
        self.show()

    def get_pingtime(self, host):  #--- get ping time of live computer

        ping = subprocess.Popen(["ping", "-n", "1", host], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        
        out, error = ping.communicate()
        out = str(out).replace("\\r\\n", "")
        temp = out.split("ms")
        temp1 = temp[3]
        temp2 = temp1.split(" ")
        result = temp2[3]
        
        return result

    def onReload(self): #--- display information of remote computer
        
        self.model = self.createMailModel(self)
        self.dataView.setModel(self.model)
      
        for data in serverdata:
            itemData = data.split(":")
            cn = pycountry.countries.get(alpha_2=itemData[0])
            countryname = cn.name
            amount = int(itemData[8])
            GB = round(amount/int(1024*1024*1024), 2)
            self.addMail(self.model, './images/'+ itemData[0].lower() +'/30.png',countryname+"/"+itemData[1], itemData[2], itemData[3], itemData[4], './icons/'+ itemData[5] + '.png', itemData[5], itemData[6], itemData[7], str(GB),itemData[9])
    
    def addMail(self,model, nflag,country, ipaddress,ss_name, status, os_logo, os, cpu, cpu_core, ram, ping):
        
        icon = QIcon()
        icon.addPixmap(QPixmap(nflag))
        logo = QIcon()
        logo.addPixmap(QPixmap(os_logo))
        
        item_col_0 = QStandardItem(icon, country)
        item_col_1 = QStandardItem(ipaddress)
        item_col_2 = QStandardItem(ss_name)
        item_col_3 = QStandardItem(status)
        item_col_4 = QStandardItem(logo, os)
        item_col_5 = QStandardItem(cpu)
        item_col_6 = QStandardItem(cpu_core)
        item_col_7 = QStandardItem(ram)
        item_col_8 = QStandardItem(ping)
        
        model.appendRow([item_col_0, item_col_1,item_col_2,item_col_3,item_col_4,item_col_5,item_col_6,item_col_7, item_col_8])

#=========== Refresh button process block ==================        
    def execute_Refresh(self): 
        
        splash.show()
        progressBar.setMaximum(255)
        new_serverdata = []
        
        for i in range(1, 254):
            host = self.subnet_mask + ".%d" % i
            data = AgentClient.client_program(host)  #--- get information of remote computer from AgentClient module again
                        
            if data != "0":
                pi = self.get_pingtime(host)
                data = data+":"+str(pi)
                new_serverdata.append(data)
        
            progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                app.processEvents()
        
        for old_item in serverdata:  #--- update new data 
            k = 0
            for new_item in new_serverdata:
                old1 = old_item.split(":")
                oldip = old1[2]
                new1 = new_item.split(":")
                newip = new1[2]                
                if oldip == newip:
                    break
                k = k + 1
            if k == len(new_serverdata):
                item = old_item.replace("Connected", "Disconnected")
                new_serverdata.append(item)
        
        serverdata.clear()

        for i in range(0, len(new_serverdata)):
            serverdata.append(new_serverdata[i])

        self.onReload()  #--- display new data on GUI
       
        splash.hide()
        self.show()

#=========== IP lookup button process block ==================
    def execute_IPlookup(self):     #---- IP lookup Diaglog GUI
        dlgEdit = QDialog()
        dlgEdit.setWindowTitle("IP Lookup")
        dlgEdit.setWindowIcon(QIcon("./icons/iplookup.png"))
        dlgEdit.resize(600, 300)

        # getservIP GUI   ( get IP from domain address)
        self.dnsName = QLabel(dlgEdit)       
        self.dnsName.setText("Target WebSite Domain")
        self.dnsName.move(20, 12)
        
        self.tagDns = QLineEdit(dlgEdit)
        self.tagDns.setPlaceholderText('google.com')
        self.tagDns.setReadOnly(False)
        self.tagDns.setEnabled(True)      
        self.tagDns.move(20, 30)
        self.tagDns.resize(170, 25)
        
        Subm1 = QPushButton('Submit', dlgEdit)
        Subm1.resize(80,25)
        Subm1.move(200, 30)
        Subm1.clicked.connect(self.submit1_click)

        self.ipValue = QTextEdit(dlgEdit)       
        self.ipValue.move(0, 60)
        self.ipValue.resize(300, 240)

        # Whois GUI ( get informaion corresponding to IP)
        self.ipAdrr = QLabel(dlgEdit)       
        self.ipAdrr.setText("Target IP Address")
        self.ipAdrr.move(320, 12)
        
        self.tagIP = QLineEdit(dlgEdit)
        self.tagIP.setPlaceholderText('216.58.200.46')

        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"   # IP addres validation ( regular expression )
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self)
        self.tagIP.setValidator(ipValidator)
        
        self.tagIP.setReadOnly(False)
        self.tagIP.setEnabled(True)      
        self.tagIP.move(320, 30)
        self.tagIP.resize(170, 25)
        
        Subm2 = QPushButton('Submit', dlgEdit)
        Subm2.resize(80,25)
        Subm2.move(500, 30)
        Subm2.clicked.connect(self.submit2_click)

        self.ipInfo = QTextEdit(dlgEdit)       
        self.ipInfo.move(300, 60)
        self.ipInfo.resize(300, 240)
   
        dlgEdit.exec_() 

    def submit1_click(self):   #---  getservIP processing

        tagDns = ""
        tagDns = self.tagDns.text()  #--- get domain address from LineEdit()

        # type website domain address
        if tagDns == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type website domain.")
            msg.exec_()
        else:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            
            ipResult = IP_Lookup.func_getservip(tagDns)   #--- get IP from IP_Lookup module
            
            self.ipValue.append("  " + ipResult)
            self.ipValue.append("")
        
            QApplication.restoreOverrideCursor() 
        
    def submit2_click(self):  #--- whois processing
       
        tagIP = ""
        tagIP = self.tagIP.text()  #--- get ip from LineEdit()
        
        # IP validation
        numItem = tagIP.split(".")
        if len(numItem) != 4 or tagIP == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type IP address.")
            msg.exec_()
        elif numItem[3] == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type IP address.")
            msg.exec_()        
        else:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            self.ipInfo.append("Detail Information on " + tagIP)
            getResult = IP_Lookup.func_whois(tagIP)     # get information from IP_Lookup module
            if getResult == []:
                self.ipInfo.append("   No result.")
            else:
                self.ipInfo.append("  " + "IP:" +"\t " + getResult[0])
                self.ipInfo.append("  " + "City:" +"\t " + getResult[1])
                self.ipInfo.append("  " + "Region:" +"\t " + getResult[2])
                self.ipInfo.append("  " + "Country:" +"\t " + getResult[3])
                self.ipInfo.append("  " + "Location:" +"\t " + getResult[4])
                self.ipInfo.append("  " + "Postal:" +"\t " + getResult[5])
                self.ipInfo.append("")
        
            QApplication.restoreOverrideCursor() 
        
#=========== MAC Vendor button process block ==================
    def execute_MACvendor(self):   #--- MAC Vendor GUI
        
        dlgEdit = QDialog()
        dlgEdit.setWindowTitle("Mac Vendor")
        dlgEdit.setWindowIcon(QIcon("./icons/default.png"))
        dlgEdit.resize(600, 300)

        self.ipName = QLabel(dlgEdit)       
        self.ipName.setText("MAC Address:")
        self.ipName.move(20, 25)
        
        self.mac = QLineEdit(dlgEdit)
        self.mac.setPlaceholderText('30-B4-9E-F1-C1-A5')
        self.mac.setReadOnly(False)
        self.mac.setEnabled(True)      
        self.mac.move(100, 20)
        self.mac.resize(170, 25)
        
        self.efName = QTextEdit(dlgEdit)       
        self.efName.move(0, 50)
        self.efName.resize(600, 250)

        Scan = QPushButton('Submit', dlgEdit)
        Scan.resize(80,25)
        Scan.move(500, 20)
        Scan.clicked.connect(self.macvendor_click)
           
        dlgEdit.exec_() 

    def macvendor_click(self): #--- mac vendor processing
        
        mac = ""
        mac = self.mac.text()  #--- get mac from LineEdit()
        # mac validation
        if len(mac) < 6 or mac == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type MAC address.")
            msg.exec_()
        else:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            self.efName.append("Vendor Information on " + mac)
            vendorInfo = Mac_Vendor.getMacVendor(mac)          #--- get vendor informaion from Mac_Vendor module
            strven = str(vendorInfo)
            errcheck  =strven.split(":")
            print(errcheck)
            if errcheck[0] == "{'error'":
                self.efName.append("   Incorrect MAC address.")
            else:
                self.efName.append("   Address:" + "\t " + vendorInfo['address'])
                self.efName.append("")
                self.efName.append("   Company:" + "\t " + vendorInfo['company'])
                self.efName.append("   Country:" + "\t " + vendorInfo['country'])
                self.efName.append("   End_Hex:" + "\t " + vendorInfo['end_hex'])
                self.efName.append("   Mac_Prefix:" + "\t " + vendorInfo['mac_prefix'])
                self.efName.append("   Start_Hex:" + "\t " + vendorInfo['start_hex'])
                self.efName.append("   Type:" + "\t " + vendorInfo['type'])
            self.efName.append("")
        
            QApplication.restoreOverrideCursor() 

#=========== PopUP Menu  process block ==================        
    def openMenu(self, position):  #--- popup menu main GUI
        
        menu = QMenu()

        ipscanItem = QAction(QIcon("./icons/IPScan.png"), "&IPScan", self)
        menu.addAction(ipscanItem)
        ipscanItem.triggered.connect(self.execute_ipscan)    #--- click ipscan menu

        portscanItem = QAction(QIcon("./icons/PortScan.png"), "&PortScan", self)
        menu.addAction(portscanItem)
        portscanItem.triggered.connect(self.execute_portscan)  #--- click port scan menu
        
        reverseItem = QAction(QIcon("./icons/ReverseShell.png"), "&ReverseShell", self)
        menu.addAction(reverseItem)
        reverseItem.triggered.connect(self.execute_reverse_shell) #--- click reverse shell menu

        remoteItem = QAction(QIcon("./icons/RemoteDesktop.png"), "&RemoteDesktop", self)
        menu.addAction(remoteItem)
        remoteItem.triggered.connect(self.execute_RDC)    #--- click remote desktop menu

        menu.exec_(self.dataView.viewport().mapToGlobal(position))
    
    #------- ip scan procee block ---------
    def execute_ipscan(self):  # ip scan diaglog GUI
        
        dlgEdit = QDialog()
        dlgEdit.setWindowTitle("IP Scan")
        dlgEdit.setWindowIcon(QIcon("./icons/IPScan.png"))
        dlgEdit.resize(600, 300)

        self.ipName = QLabel(dlgEdit)       
        self.ipName.setText("Subnet: ")
        self.ipName.move(20, 25)
        
        self.ips = QLineEdit(dlgEdit)
        self.ips.setPlaceholderText('192.168.1.0/24')
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"   # ips validation ( regular expression )
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "\\/" + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self)
        self.ips.setValidator(ipValidator)
        self.ips.setReadOnly(False)
        self.ips.setEnabled(True)      
        self.ips.move(70, 20)
        self.ips.resize(170, 25)
        
        self.comments = QLabel(dlgEdit)       
        self.comments.setText("Ex: 192.168.1.0/24")
        self.comments.move(245, 25)

        self.efName = QTextEdit(dlgEdit)       
        self.efName.move(0, 50)
        self.efName.resize(600, 250)

        Scan = QPushButton('Scan', dlgEdit)
        Scan.resize(80,25)
        Scan.move(500, 20)
        Scan.clicked.connect(self.ipscan_click)   # call ip scan process
           
        dlgEdit.exec_() 

    def ipscan_click(self):  #--- ip scan process
        
        ips = ""
        ips = self.ips.text()       #--- get ips from LineEdit()
        #--- ips validation
        numItem = ips.split(".")
        if len(numItem) != 4 or ips == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type correct subnet...")
            msg.exec_()
        elif numItem[3] == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type correct subnet...")
            msg.exec_()            
        # display ip scan result
        else:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            self.efName.append("IP Address and MAC on " + ips)
            
            devices = IP_Scan.arp(str(ips))         #--- ip scan process from IP_Scan module
            rcv = str(devices)
            print(rcv)
            ans = rcv.split(":")
            if ans[5] == "0>":
                self.efName.append("  No result.")
            else:
                for snd,rcv in devices:
                    self.efName.append("  " + rcv.psrc + "\t" + ":   " + rcv.src)
            self.efName.append("")
                
            QApplication.restoreOverrideCursor() 

    #------- port scan procee block ---------
    def execute_portscan(self):  #---  GUI-dialog for port scan
        
        dlgEdit = QDialog()
        dlgEdit.setWindowTitle("Port Scan")
        dlgEdit.setWindowIcon(QIcon("./icons/PortScan.png"))
        dlgEdit.resize(600, 300)

        self.ipName = QLabel(dlgEdit)       
        self.ipName.setText("Host IP:")
        self.ipName.move(20, 25)
        
        self.hostip = QLineEdit(dlgEdit)
        self.hostip.setPlaceholderText('192.168.1.131')
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"   # Part of the regular expression
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self)
        self.hostip.setValidator(ipValidator)
        self.hostip.setReadOnly(False)
        self.hostip.setEnabled(True)      
        self.hostip.move(70, 20)
        self.hostip.resize(170, 25)
        
        self.efName = QTextEdit(dlgEdit)       
        self.efName.move(0, 50)
        self.efName.resize(600, 250)

        Scan = QPushButton('Scan', dlgEdit)
        Scan.resize(80,25)
        Scan.move(500, 20)
        Scan.clicked.connect(self.portscan_click)       #--- call port scan process
           
        dlgEdit.exec_() 

    def portscan_click(self):  #---  port scan process
        shost = ""
        shost = self.hostip.text()  #--- get host ip from GUI LineEdit()
        
        #--- IP address validation processing
        numItem = shost.split(".")
        if len(numItem) != 4 or shost == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type correct host IP.")
            msg.exec_()
        elif numItem[3] == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type correct host IP.")
            msg.exec_()            
        #---- get open port and display 
        else:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            self.efName.append("Open Ports on " + shost)
            port = ""
            openPorts = Port_Scan.port_scan(str(shost))  #--- call function of Port_Scan module 
            if openPorts == []:
                self.efName.append( "  No result.")
            else:
                for i in openPorts:
                    port = port + "  " + i
                self.efName.append("  " + port)
                self.efName.append("")
        
            QApplication.restoreOverrideCursor() 

#========== reverse shell  processing block  ================
    def execute_reverse_shell(self):  #--- run reverse shell program
        window_command = "cmd.exe /c start cmd.exe /k python Reverse_Shell.py"
        Popen(window_command)

#========== remote desktop connection  block  ================    
    def execute_RDC(self):  #--- run remote desktop client program
        window_command = "python RDC_Client.py"
        Popen(window_command)

# Function to get Local IP address 
    # def get_Host_name_IP(self): 
    #     interfaces = netifaces.interfaces()
    #     gws=netifaces.gateways()
    #     ss = gws['default']
    #     dd = ss[2]
    #     aa = dd[0].split('.')
    #     subnet = aa[0]+"."+aa[1]+"."+aa[2]
    #     UserIP = []
    #     ii = 0
    #     for i in interfaces:        
    #         if i == 'lo':
    #             continue
    #         iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
    #         if iface != None:
    #             for j in iface:
    #                 UserIP.append(j['addr'])
    #         ii = ii+1
    #     for ip in UserIP:
    #         sub = ip.split(".")
    #         subip = sub[0]+"."+sub[1]+"."+sub[2]
    #         if subip == subnet:
    #             lan = ip
    #     # array = [lan, subnet, wan]
    #     array = [lan, subnet]
    #     return array

    def get_Host_name_IP(self):  #--- get IP address and subnet of host(this computer)
            
        hostname = socket.gethostname()
        host = socket.gethostbyname(hostname)
        print(host)

        sub = host.split(".")
        subnet = sub[0]+"."+sub[1]+"."+sub[2]

        array = [host, subnet]
        return array

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    #--- setting darkstyle sheet on main window
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(dark_stylesheet)

    #--- splash process
    splash_pix = QPixmap('logo.ico')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    progressBar = QProgressBar(splash)
    progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)

    splash.show()
    splash.showMessage("<h1><font color='green'>Coinpaign Scanning...</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)
    #-------------------
    ex = App()
    sys.exit(app.exec_())
