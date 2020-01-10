# ###################################################################################################################
# Deletes Work Managers & Thread Constraints
# Usage :   DeleteWorkManagers.py   WorkManagers Properties file
#           
# ####################################################################################################################
 
import sys
#read properties file
 
if len(sys.argv) != 2:
    print "Invalid Arguements :: Usage DeleteWorkManagers.py <WorkManagers Properties file>"
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
stMBean=getMBean("/SelfTuning/"+DOMAIN)
for workManager in WORK_MANAGER_ARRAY:
    wmMBean=getMBean("/SelfTuning/"+DOMAIN+"/WorkManagers/"+workManager['NAME'])
    if wmMBean != None: 
        stMBean.destroyWorkManager(wmMBean)
for mtConstraint in MAX_THREADS_CONSTRAINT_ARRAY:
     
    mtcMBean=getMBean("/SelfTuning/"+DOMAIN+"/MaxThreadsConstraints/"+mtConstraint['NAME'])
    if mtcMBean != None:
        print "destroying max threads constraints...."
        stMBean.destroyMaxThreadsConstraint(mtcMBean)
        print "destroyed max threads constraint"
 
activate()
exit()