#WLST script location - /u01/app/oracle/middleware/oracle_common/common/bin/wlst.sh
domain="/u01/data/domains//weblogic_domain"
service = weblogic.security.internal.SerializedSystemIni.getEncryptionService(domain)
encryption = weblogic.security.internal.encryption.ClearOrEncryptedService(service)
print encryption.decrypt("{AES}mkvF3N7+v8d2usadkjcLQkAcuQcTDbnJA3/WV4EXxhs=")