# snmpwalk

> SNMP query tool.
> More information: <https://manned.org/snmpwalk>.

- Query the system information of a remote host using SNMPv1 and a community string:

`snmpwalk -v 1 -c {{community}} {{ip}}`

- Query system information on a remote host by OID using SNMPv2 on a specified port:

`snmpwalk -v 2c -c {{community}} {{ip}}:{{port}} {{oid}}`

- Query system information on a remote host by OID using SNMPv3 and authentication without encryption:

`snmpwalk -v 3 -l {{authNoPriv}} -u {{username}} -a {{MD5|SHA}} -A {{passphrase}} {{ip}} {{oid}}`

- Query system information on a remote host by OID using SNMPv3, authentication, and encryption:

`snmpwalk -v 3 -l {{authPriv}} -u {{username}} -a {{MD5|SHA}} -A {{auth_passphrase}} -x {{DES|AES}} -X {{enc_passphrase}} {{ip}} {{oid}}`

- Query system information on a remote host by OID using SNMPv3 without authentication or encryption:

`snmpwalk -v 3 -l {{noAuthNoPriv}} -u {{username}} {{ip}} {{oid}}`

- Display help:

`snmpwalk {{[-h|--help]}}`
