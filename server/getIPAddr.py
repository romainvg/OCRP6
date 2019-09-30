#################################################################################
#                                                                               #
#  setIPAddr.py		                                                        #
#  										#
#  The software is licensed Creative Commons CC-BY-NC-SA. Under this agreement  #
#  you are authorized to use, share on the same rights or edit this software    #
#  for personnal purpose only. You are not allow to sell this software.         #
#                                                                               #
#    Official Website : https://coinpaign.com                                   #
#    Contact : romain.guihot@gmail.com     					#

#  This module is installed in computers to be managed by Remote Administrator. #
#  This is used in RDC_Server.py                                                # 
#  Function:                                                                    #
#     Get IP address of computer                                                #
#                                                                               #
#################################################################################

import socket 

def getIP( ):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('www.google.com', 80))
	addr = s.getsockname( )[0]  
	s.close( )  
	return addr
