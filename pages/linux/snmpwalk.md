# snmpwalk

> SNMP query tool.
> More information: <https://linux.die.net/man/1/snmpwalk>.

- Query target system information using SNMPv1 and community string:

`snmpwalk -v1 -c {{community}} {{ip}}`

- Query specific target system information by OID using SNMPv2 on a specified port:

`snmpwalk -v2c -c {{community}} {{ip}}:{{port}} {{oid}}`

- Query specific target system information by OID using SNMPv3 and authentication without encryption:

`snmpwalk -v3 -l {{authNoPriv}} -u {{username}} -a {{MD5|SHA}} -A {{passphrase}} {{ip}} {{oid}}`

- Query specific target system information by OID using SNMPv3, authentication and encryption:

`snmpwalk -v3 -l {{authPriv}} -u {{username}} -a {{MD5|SHA}} -A {{auth_passphrase}} -x {{DES|AES}} -X {{enc_passphrase}} {{ip}} {{oid}}`

- Query specific target system information by OID using SNMPv3 without authentication or encryption:

`snmpwalk -v3 -l {{noAuthNoPriv}} -u {{username}} {{ip}} {{oid}}`
