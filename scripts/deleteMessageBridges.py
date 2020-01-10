# ##########################################################################
# Creates Message Bridges
# Usage : DeleteMessageBridges.py <Name of Properties file >
# #########################################################################
import sys
#read properties file
 
if len(sys.argv) != 2:
    print "Invalid Arguements :: Usage DeleteMessageBridges.py <Message Bridge Properties file>"
    exit()
try:
    print "Load properties file"
    properties=sys.argv[1]
    file=open(properties,'r')
    print "Read properties file"
    exec file
    print "Execute properties file"
    file.close
except:
    exit()
#Connect
 
connect(USER,PASSWORD,ADMIN_URL)
edit()
startEdit()
bdgDestMBean=getMBean("/JMSBridgeDestinations/")
bdgMBean=getMBean("/MessagingBridges/")
for msgBridge in MSGBRIDGE_ARRAY:
      
    destinations = (msgBridge['SOURCE_DEST'],msgBridge['TARGET_DEST'])
     
    bdgInstanceMBean=getMBean("/MessagingBridges/"+msgBridge['NAME'])
    if bdgInstanceMBean != None:
        bdgMBean.destroyMessagingBridge(bdgInstanceMBean)
         
    for dest in destinations :
        destMBean=getMBean("/JMSBridgeDestinations/"+dest['NAME'])
        if destMBean != None: 
            bdgDestMBean.destroyJMSBridgeDestination(destMBean)
         
activate()
exit()