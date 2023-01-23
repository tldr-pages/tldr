# snmpwalk

> SNMP-lekérdező eszköz. További információ: <https://manned.org/snmpwalk>.

- Egy távoli állomás rendszerinformációinak lekérdezése az SNMPv1 és egy közösségi karakterlánc segítségével:

`snmpwalk -v1 -c {{community}} {{ip}}`

- Egy távoli állomás rendszerinformációinak lekérdezése OID alapján SNMPv2 használatával egy megadott porton:

`snmpwalk -v2c -c {{community}} {{ip}}:{{port}} {{oid}}`

- Távoli állomás rendszerinformációinak lekérdezése OID alapján SNMPv3 és titkosítás nélküli hitelesítés használatával:

`snmpwalk -v3 -l {{authNoPriv}} -u {{username}} -a {{MD5|SHA}} -A {{passphrase}} {{ip}} {{oid}}`

- Egy távoli állomás rendszerinformációinak lekérdezése OID alapján SNMPv3, hitelesítés és titkosítás használatával:

`snmpwalk -v3 -l {{authPriv}} -u {{username}} -a {{MD5|SHA}} -A {{auth_passphrase}} -x {{DES|AES}} -X {{enc_passphrase}} {{ip}} {{oid}}`

- Egy távoli állomás rendszerinformációinak lekérdezése OID szerint SNMPv3 használatával, hitelesítés vagy titkosítás nélkül:

`snmpwalk -v3 -l {{noAuthNoPriv}} -u {{username}} {{ip}} {{oid}}`
