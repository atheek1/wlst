# ##########################################################################
# Creates Work Managers & Thread Constraints
# Usage : CreateWorkManagers.py <Name of Properties file >
# #########################################################################
import sys
#read properties file
 
if len(sys.argv) != 2:
    print "Invalid Arguements :: Usage CreateWorkManagers.py <WorkManagers Properties file>"
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
wmMBean=getMBean("/SelfTuning/"+DOMAIN)
if wmMBean is None:
        print "@@@ Invalid DOMAIN Name '"+DOMAIN+"'"
        exit()
 
for maxThreadsConst in MAX_THREADS_CONSTRAINT_ARRAY :
    if (maxThreadsConst['TARGET_TYPE']=="SERVER"):
        targetMB=getMBean("/Servers/"+maxThreadsConst['TARGET'])
    if (maxThreadsConst['TARGET_TYPE']=="CLUSTER"):
        targetMB=getMBean("/Clusters/"+maxThreadsConst['TARGET'])
    if targetMB is None:
        print "@@@ Invalid MAX THREADS CONSTRAINT Target '"+maxThreadsConst['TARGET']+"'"
        exit()
    if getMBean("/SelfTuning/"+DOMAIN+"/MaxThreadsConstraints/"+maxThreadsConst['NAME']) is None:       
        maxThreadConstInstance=wmMBean.createMaxThreadsConstraint(maxThreadsConst['NAME'])
        maxThreadConstInstance.addTarget(targetMB)
        maxThreadConstInstance.setCount(maxThreadsConst['COUNT'])
 
for workManager in WORK_MANAGER_ARRAY :
    if (workManager['TARGET_TYPE']=="SERVER"):
        targetMB=getMBean("/Servers/"+workManager['TARGET'])
    if (workManager['TARGET_TYPE']=="CLUSTER"):
        targetMB=getMBean("/Clusters/"+workManager['TARGET'])
    if targetMB is None:
        print "@@@ Invalid Work Manager Target '"+workManager['TARGET']+"'"
        exit()
    if getMBean("/SelfTuning/"+DOMAIN+"/WorkManagers/"+workManager['NAME']) is None:        
        workManagerInstance=wmMBean.createWorkManager(workManager['NAME'])
        workManagerInstance.addTarget(targetMB)
        workManagerInstance.setMaxThreadsConstraint(wmMBean.lookupMaxThreadsConstraint(workManager['MAX_THREADS_CONSTRAINT']))
     
activate()
exit()