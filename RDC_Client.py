####################################################################################
#                                                                                  #
#  RDC_Client.py                                                                   #
#                                                                                  #
#  The software is licensed Creative Commons CC-BY-NC-SA. Under this agreement     #
#  you are authorized to use, share on the same rights or edit this software       #
#  for personnal purpose only. You are not allow to sell this software.            #
#                                                                                  #
#  Official Website : https://coinpaign.com                                        #
#  Contact : romain.guihot@gmail.com                                               #

#  This module is installed in Remote Administrator' computer.                     #
#  This is client program for remote desktop connection through RDP protocol.      #
#  Function:                                                                       #
#     1. Client configuration GUI   (IP, password)                                 #
#     2. Send protocol message to server                                           #
#     3. Receive protocol message from server                                      #
#     4. Receive live screen data of computer to server and display them           #
#     5. Capture mouse and keyboard event and send action data to server           #
#                                                                                  #
####################################################################################

#--- standard package
import sys
import os

#--- dependent package
from twisted.internet.protocol import Protocol, Factory, ClientFactory
from twisted.python import log

from PyQt5.QtCore import Qt
from PyQt5.QtGui import  QIcon,QPixmap, QPainter
from PyQt5.QtWidgets import (QApplication, QAction, QLabel, QVBoxLayout, QWidget, QMainWindow, QStyleFactory, QMessageBox)
from PyQt5.QtWidgets import (QDialog, QGridLayout, QHBoxLayout, QPushButton, QLineEdit, QGroupBox, QFormLayout)

#--- developed sub module
import RDC_ClientProtocol as clientProtocol
import qt5reactor

srvIP = ""
srvPWD = ""

log.startLogging(sys.stdout)

app = QApplication(sys.argv)

__applib__  = os.path.dirname(os.path.realpath(__file__))
__appicon__ = os.path.dirname(os.path.realpath(__file__))

qt5reactor.install( )

#-----------------------#
##   Initial Dialog    ##
#-----------------------#
class InitialDlg(QDialog):
    """
    The InitialDlg provide GUI  to Input Remote Desktop Server' IP and Password
    
    """
    def __init__(self):

        super().__init__()

        self.setupUI( )

        mainLayout = QGridLayout( )
        mainLayout.addWidget(self.groupbox,  0, 0)
        mainLayout.addLayout(self.butLayout, 2, 0)
        self.setLayout(mainLayout)

        # add Start & quit action
        self.connectBut.clicked.connect(self.onConnect)
        self.quitBut.clicked.connect(self.quit)

    def setupUI(self):

        self.setFixedSize(320, 200)
        self.setWindowTitle('Remote Desktop Connection')
        self.setWindowIcon(QIcon('./icons/RemoteDesktop.png'))

        self.groupbox = QGroupBox( )
        formLayout    = QFormLayout( )

        self.blk1       = QLabel() 
        self.addrEdit   = QLineEdit( )
        self.addrEdit.setPlaceholderText('192.168.1.131')
        self.blk2       = QLabel() 
        self.passwdEdit = QLineEdit( )
        self.passwdEdit.setEchoMode(QLineEdit.Password)
        self.blk3       = QLabel() 
       
        formLayout.addRow(QLabel(''),  self.blk1)
        formLayout.addRow(QLabel('Computer'), self.addrEdit)
        formLayout.addRow(QLabel(''),  self.blk2)
        formLayout.addRow(QLabel('Password'), self.passwdEdit)
        formLayout.addRow(QLabel(''),  self.blk3)

        self.groupbox.setLayout(formLayout)

        self.butLayout     = QHBoxLayout( )
        self.connectBut    = QPushButton('Connect')
        self.quitBut       = QPushButton('Quit')
        self.butLayout.addWidget(self.connectBut)
        self.butLayout.addWidget(self.quitBut)

        self.show()

    # Processing to connect to server
    def onConnect(self):

        global srvIP, srvPWD

        srvIP = str(self.addrEdit.text())
        srvPWD  = str(self.passwdEdit.text())

        ## IP & Password Validation
        ip = srvIP.split(".")
        if len(ip) != 4 or srvIP == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type correct IP and Password")
            msg.exec_()
        elif ip[3] == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type correct IP and Password")
            msg.exec_()
        elif len(srvPWD) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please type correct Password")
            msg.exec_()
        else:
            # self.close()
            self.hide()

            mydesktop.show( )
            mydesktop.connectionStart()

    def quit(self):
        self.close()

class RDCToGUI(clientProtocol.rdc):
    def __init__(self):
        clientProtocol.rdc.__init__(self)
        self.num = 0
        self.count = 0

    def connectionMade(self):
        self.factory.readyConnection(self)

    def vncRequestPassword(self):
        password = self.factory.password
        if not password:
            password = input( )
        self.sendPassword(password)

    def commitFramebufferUpdate(self, framebuffer):
        self.factory.display.updateFramebuffer(framebuffer)
        self.framebufferUpdateRequest(width=self.factory.display.width, height=self.factory.display.height)


class RDCFactory(clientProtocol.RDCFactory):
    def __init__(self, display=None, password=None, shared=0):
        clientProtocol.RDCFactory.__init__(self, password, shared)
        self.display  = display
        self.protocol = RDCToGUI

    def buildProtocol(self, addr):
        return clientProtocol.RDCFactory.buildProtocol(self, addr)

    def readyConnection(self, client):
        self.display.readyDisplay(client)
        
    def clientConnectionFailed(self, connector, reason):
        log.msg("Client connection failed!. (%s)" % reason.getErrorMessage( ))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Failure")
        msg.setText("Please type correct IP and Password")
        msg.exec_()
        
        # reactor.stop()
        
        mydesktop.hide()
        initdlg.show()
        
    def clientConnectionLost(self, connector, reason):
        log.msg("Client connection lost!. (%s)" % reason.getErrorMessage( ))
        reactor.stop( )


class Display(QWidget):
    """
    this class for display remoteframebuffer and get the client events
    and then send the events to server, the include keyEvent, pointerEvent,
    mouseMoveEvent, clipboardEvent.
    """
    def __init__(self, parent=None):
        super(Display, self).__init__(parent)
        self.resize(1390, 780)
        self._pixelmap          = QPixmap( )
        self._remoteframebuffer = b""
        self._clipboard         = QApplication.clipboard( )
        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.StrongFocus)
        self.clientProtocol = None
        self.parent = parent

    def readyDisplay(self, protocol):
        self.clientProtocol = protocol
    
    # display server screen data on client screen
    def paintEvent(self, event):
        """
        paint frame buffer in widget
        """
        if self._remoteframebuffer:
           self._pixelmap.loadFromData(self._remoteframebuffer)
           painter = QPainter(self)
           painter.drawPixmap(0, 0, self._pixelmap)
        self.update( )
    
    # update server screen data
    def updateFramebuffer(self, pixelmap):
        self._remoteframebuffer = pixelmap

    # update keypress event
    def keyPressEvent(self, event):
        key  = event.key( )
        print(key)
        flag = event.type( ) 
        if self.clientProtocol is None: return
        self.clientProtocol.keyEvent(key, flag)
        self.update( )

    # update mousepress event
    def mousePressEvent(self, event):
        x, y   = (event.pos( ).x( ), event.pos( ).y( )) 
        button = event.button( )
        print(button)
        flag   = event.type( )
        if self.clientProtocol is None: return #self.clientProtocol = self.parent.client.clientProto
        self.clientProtocol.pointerEvent(x, y, button, flag)
        print(self.clientProtocol.pointerEvent)

    # update mouse release event
    def mouseReleaseEvent(self, event):
        x, y   = (event.pos( ).x( ), event.pos( ).y( )) 
        button = event.button( )
        flag   = event.type( )
        if self.clientProtocol is None: return #self.clientProtocol = self.parent.client.clientProto
        self.clientProtocol.pointerEvent(x, y, button, flag)

    # update mouse move event
    def mouseMoveEvent(self,  event):
        x, y   = (event.pos( ).x( ), event.pos( ).y( )) 
        button = event.button( )
        flag   = event.type( )
        if self.clientProtocol is None: return #self.clientProtocol = self.parent.client.clientProto
        self.clientProtocol.pointerEvent(x, y, button, flag)
        
    # update resize event
    def resizeEvent(self, event):
        """
        the remote framebuffer's size is according the client viewer size
        this may reduce the size of the images can be
        """
        size = event.size( )
        self.width, self.height = (size.width(), size.height())


class myDesktopViewer(QMainWindow):
    def __init__(self,  parent=None):
        super(myDesktopViewer, self).__init__(parent)
        self.display = Display(self)
        self.setupUI( )

    # setup remote desktop connection UI
    def setupUI(self):

        global srvIP, srvPWD

        self.setWindowTitle('Coinpaign : Remote Desktop Connection')
        self.setWindowIcon(QIcon('./icons/RemoteDesktop.png'))
        # self.resize(800, 600)
        self.showMaximized()
        QApplication.setStyle(QStyleFactory.create('cleanlooks'))
        QApplication.setPalette(QApplication.style( ).standardPalette())

        # add adction on application
        self.startAction = QAction(QIcon(os.path.join(__appicon__, 'icons', 'Start.png')), 'Start', self)
        self.stopAction  = QAction(QIcon(os.path.join(__appicon__, 'icons', 'Stop.png')),  'Stop',  self)
        self.startAction.setToolTip('Start connection')
        self.stopAction.setToolTip('Stop connection')
        self.startAction.triggered.connect(self.connectionStart)
        self.stopAction.triggered.connect(self.connectionStop)

        # add a toolbar
        self.toolbar = self.addToolBar('')
        self.toolbar.addAction(self.stopAction)
        self.toolbar.addAction(self.startAction)

        displayWidget = QWidget( )
        vbox   = QVBoxLayout(displayWidget)
        vbox.addWidget(self.display)
        self.setCentralWidget(displayWidget)

    def connectionStart(self):
        self.client = RDCFactory(display=self.display, password=srvPWD)
        reactor.connectTCP(srvIP, 5000, self.client)
        
    def connectionStop(self):
        reactor.stop( )

    def closeEvent(self, event):
        self.connectionStop( )
        exit( )

if __name__ == '__main__':
    from twisted.internet import reactor
    initdlg = InitialDlg()
    mydesktop = myDesktopViewer()
    mydesktop.hide( )
    reactor.run( ) # enter mainloop
    sys.exit(app.exec_()) 
