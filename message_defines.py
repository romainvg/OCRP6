#################################################################################
#                                                                               #
#  message_defines.py                                                           #
#                                                                               #
#  This module is installed in computers to be managed by Remote Administrator. #
#  This is used in RDC_ServerProtocol.py and RDC_ClientProtocol.py              # 
#  Function:                                                                    #
#     define message types for RDP protocol                                     #
#                                                                               #
#################################################################################

class protocolMessageTypes: 
    pass

messageTypes = protocolMessageTypes( )

messageTypes.AUTHENTICATION     = 0
messageTypes.INITIALIZATION     = 1  
messageTypes.FRAME_UPDATE       = 2 
messageTypes.KEY_EVENT          = 3
messageTypes.POINTER_EVENT      = 4
messageTypes.COPY_TEXT          = 5
messageTypes.CUT_TEXT           = 6
messageTypes.TEXT_MESSAGE       = 7
messageTypes.AUTH_RESULT        = 8 
