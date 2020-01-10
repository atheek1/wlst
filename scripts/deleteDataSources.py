# ##########################################################################
# Deletes Data Sources
# Usage : DeleteDataSources.py <Name of Properties file >
# #########################################################################
import sys
#read properties file
 
if len(sys.argv) != 2:
    print "Invalid Arguements :: Usage DeleteDataSources.py <DataSource Properties file>"
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
 
jdbcSysResourceMBean=getMBean("/JDBCSystemResources/") 
for dataSource in DATASOURCE_ARRAY:
    dataSourceMBean=getMBean("/JDBCSystemResources/"+dataSource['NAME'])
    if dataSourceMBean != None:
        if (dataSource['TARGET_TYPE']=="SERVER"):
            targetMB=getMBean("/Servers/"+dataSource['TARGET'])
        if (dataSource['TARGET_TYPE']=="CLUSTER"):
            targetMB=getMBean("/Clusters/"+dataSource['TARGET'])
        if targetMB != None:    
            dataSourceMBean.removeTarget(targetMB)
        if len(dataSourceMBean.getTargets()) ==0: #No Targets 
            jdbcSysResourceMBean.destroyJDBCSystemResource(dataSourceMBean)
 
activate()      
exit()