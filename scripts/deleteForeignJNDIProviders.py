# ##########################################################################
# Delete Foreign JNDI Links
# Usage : DeleteForeignJNDIProviders.py <Name of Properties file >
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
forJNDIProviderMBean=getMBean("/ForeignJNDIProviders/")
for foreignJNDI in FOREIGN_JNDI_ARRAY:
    jndiProviderInstance=getMBean("/ForeignJNDIProviders/"+foreignJNDI['NAME'])
    if jndiProviderInstance != None: 
        forJNDIProviderMBean.destroyForeignJNDIProvider(jndiProviderInstance)
         
activate()
exit()