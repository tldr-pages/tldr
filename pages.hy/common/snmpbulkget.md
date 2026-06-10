# snmpbulkget

> Հարցրեք MIB ծառի հաջորդ արժեքը և դրա բոլոր հարակից արժեքները:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/snmpbulkget>:.

- SNMP գործակալից պահանջեք հաջորդ արժեքը.:

`snmpbulkget -v {{version}} -c {{community}} {{ip_address}} {{oid}}`

- Ցուցադրել օբյեկտի նույնացուցիչի (OID) ամբողջական ուղին.:

`snmpbulkget -v {{version}} -c {{community}} -O f {{ip_address}} {{oid}}`

- Ցուցադրել օգնությունը.:

`snmpbulkget {{[-h|--help]}}`
