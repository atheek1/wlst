# ##########################################################################
# Creates Foreign JNDI Links
# Usage : CreateForeignJNDIProviders.py <Name of Properties file >
# #########################################################################
import sys
#read properties file
 
if len(sys.argv) != 2:
    print "Invalid Arguements :: Usage ForeignJNDIProviders.py <ForeignJNDI Properties file>"
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
 
for foreignJNDI in FOREIGN_JNDI_ARRAY:
    if (foreignJNDI['TARGET_TYPE']=="SERVER"):
        targetMB=getMBean("/Servers/"+foreignJNDI['TARGET'])
    if (foreignJNDI['TARGET_TYPE']=="CLUSTER"):
        targetMB=getMBean("/Clusters/"+foreignJNDI['TARGET'])
    if targetMB is None:
        print "@@@ Invalid Foreign JNDI Provider Target '"+foreignJNDI['TARGET']+"'"
        exit()
    if getMBean("/ForeignJNDIProviders/"+foreignJNDI['NAME']) is None:      
        foreignJNDIInstance=create(foreignJNDI['NAME'],"ForeignJNDIProvider")
        foreignJNDIInstance.addTarget(targetMB)
        foreignJNDIInstance.setInitialContextFactory(foreignJNDI['INITIAL_CONTEXT_FACTORY'])
        foreignJNDIInstance.setProviderURL(foreignJNDI['PROVIDER_URL'])
        foreignJNDIInstance.setUser(foreignJNDI['USER'])
        foreignJNDIInstance.setPassword(foreignJNDI['PASSWORD'])
     
        for foreignLink in foreignJNDI['LINKS_ARRAY']:
            foreignLinkInstance=foreignJNDIInstance.createForeignJNDILink(foreignLink['NAME'])
            foreignLinkInstance.setLocalJNDIName(foreignLink['LOCAL_JNDI'])
            foreignLinkInstance.setRemoteJNDIName(foreignLink['REMOTE_JNDI'])
     
         
activate()
exit()