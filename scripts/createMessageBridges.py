# ##########################################################################
# Creates Message Bridges
# Usage : CreateMessageBridges.py <Name of Properties file >
# #########################################################################
import sys
#read properties file
 
if len(sys.argv) != 2:
    print "Invalid Arguements :: Usage CreateMessageBridges.py <Message Bridge Properties file>"
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
for msgBridge in MSGBRIDGE_ARRAY:
      
    destinations = (msgBridge['SOURCE_DEST'],msgBridge['TARGET_DEST'])
     
    for dest in destinations :
        if getMBean("/JMSBridgeDestinations/"+dest['NAME']) is None:
            jmsBridgeDestination=create(dest['NAME'],"JMSBridgeDestination")
            jmsBridgeDestination.setAdapterJNDIName(dest['ADAPTER_JNDI'])
            jmsBridgeDestination.setInitialContextFactory(dest['INITIAL_CONTEXT_FACTORY'])
            jmsBridgeDestination.setConnectionFactoryJNDIName(dest['CONNECTION_FACTORY'])
            jmsBridgeDestination.setDestinationJNDIName(dest['DESTINATION'])
            jmsBridgeDestination.setDestinationType(dest['DESTINATION_TYPE'])
    if getMBean("/MessagingBridges/"+msgBridge['NAME']) is None:
        messagingBridgeInstance=create(msgBridge['NAME'],"MessagingBridge")
     
        if (msgBridge['TARGET_TYPE']=="SERVER"):
            targetMB=getMBean("/Servers/"+msgBridge['TARGET'])
        if (msgBridge['TARGET_TYPE']=="CLUSTER"):
            targetMB=getMBean("/Clusters/"+msgBridge['TARGET'])
 
        if targetMB is None:
            print "@@@ Invalid Message Bridge Target '"+msgBridge['TARGET']+"'"
            exit()
     
        messagingBridgeInstance.addTarget(targetMB)
        messagingBridgeInstance.setSourceDestination(getMBean("/JMSBridgeDestinations/"+msgBridge['SOURCE_DEST']['NAME']))
        messagingBridgeInstance.setTargetDestination(getMBean("/JMSBridgeDestinations/"+msgBridge['TARGET_DEST']['NAME']))
        messagingBridgeInstance.setStarted(true)
        messagingBridgeInstance.setQualityOfService(msgBridge['QOS'])
        messagingBridgeInstance.setAsyncEnabled(false)
        messagingBridgeInstance.setPreserveMsgProperty(true)
        messagingBridgeInstance.setReconnectDelayMaximum(5)
        messagingBridgeInstance.setTransactionTimeout(10)
     
     
activate()
 
exit()