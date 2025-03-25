# snmpbulkget

> Query the next value in the MIB tree and all of its adjacent values.
> More information: <https://manned.org/snmpbulkget>.

- Request the next value from the SNMP agent:

`snmpbulkget -v {{version}} -c {{community}} {{ip}} {{oid}}`

- Display the full Object Identifier (OID) path:

`snmpbulkget -v {{version}} -c {{community}} -O f {{ip}} {{oid}}`

- Display help:

`snmpbulkget {{[-h|--help]}}`
