#################################################################################
#                                                                               #
#  setIPAddr.py		                                                            #
#                                                                               #
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
