# snmpgetnext

> Query the next value in the MIB tree.
> More information: <https://manned.org/snmpgetnext>.

- Request the next value from the SNMP agent:

`snmpget -v {{version}} -c {{community}} {{ip}} {{oid}}`

- Display the full Object Identifier (OID) path:

`snmpget -v {{version}} -c {{community}} -O f {{ip}} {{oid}}`
