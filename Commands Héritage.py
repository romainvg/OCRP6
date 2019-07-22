import os

class Systeme:
    """"" Class pour les sytèmes d exploitation """""


    def __init__(self, ip=""):
        self.ip=""
        if ip =="":
            self.getIpAddres()
        else:
            self.ip=ip
    def getMacAddress(self):
        print("getMacAddress "+self.ip)
        return ""
    def getIpAddres(self):
        return ""

class WindowsSysteme(Systeme):
    def getMacAddress(self):
        Systeme.getMacAddress(self)
        os.system("getmac /v")

    def getIpAddres(self):
        self.ip="172.0.0.0"

osWin = WindowsSysteme()
print("osWin"+osWin.ip)
os=Systeme()
print("os"+os.ip)

"""osWin.getMacAddress()

a = Systeme("192.168.1.1")
b = Systeme("192.168.4.1")

print(a.ip)
print(b.ip)
a.getMacAddress()
b.getMacAddress()
"""




