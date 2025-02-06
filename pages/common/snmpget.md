# Exclamation mark

> Query using the SNMP protocol.
> More information: <https://manned.org/snmpget>.

- Request a single value from an snmp agent:

`snmpget -v {{version}} -c {{community}} {{ip}} {{oid}}`

- Display the full OID path:

`snmpget -v {{version}} -c {{community}} -O f {{ip}} {{oid}}`
