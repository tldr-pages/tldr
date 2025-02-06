# snmpget

> Query using the SNMP protocol.
> More information: <https://manned.org/snmpget>.

- Request a single value from the SNMP agent:

`snmpget -v {{version}} -c {{community}} {{ip}} {{oid}}`

- Display the full OID path:

`snmpget -v {{version}} -c {{community}} -O f {{ip}} {{oid}}`
