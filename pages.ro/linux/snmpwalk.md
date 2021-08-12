# snmpwalk

> instrument de interogare SNMP.
> Mai multe informaţii: <https://manned.org/snmpwalk>

- Interogarea informațiilor de sistem ale unei gazde la distanță utilizând SNMPv1 și un șir de comunitate:

`snmpwalk -v1 -c {{community}} {{ip}}`

- Interogare informații de sistem specifice pe o gazdă la distanță de OID folosind SNMPv2 pe un port specificat:

`snmpwalk -v2c -c {{community}} {{ip}}:{{port}} {{oid}}`

- Interogare informații specifice de sistem pe o gazdă la distanță de OID folosind SNMPv3 și autentificare fără criptare:

`snmpwalk -v3 -l {{authNoPriv}} -u {{username}} -a {{MD5|SHA}} -A {{passphrase}} {{ip}} {{oid}}`

- Interogare informații specifice de sistem pe o gazdă la distanță de OID folosind SNMPv3, autentificare și criptare:

`snmpwalk -v3 -l {{authPriv}} -u {{username}} -a {{MD5|SHA}} -A {{auth_passphrase}} -x {{DES|AES}} -X {{enc_passphrase}} {{ip}} {{oid}}`

- Interogare informații specifice de sistem pe o gazdă la distanță de OID folosind SNMPv3 fără autentificare sau criptare:

`snmpwalk -v3 -l {{noAuthNoPriv}} -u {{username}} {{ip}} {{oid}}`
