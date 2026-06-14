# snmpgetnext

> Հարցրեք MIB ծառի հաջորդ արժեքը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/snmpgetnext>:.

- SNMP գործակալից պահանջեք հաջորդ արժեքը.:

`snmpgetnext -v {{version}} -c {{community}} {{ip_address}} {{oid}}`

- Ցուցադրել օբյեկտի նույնացուցիչի (OID) ամբողջական ուղին.:

`snmpgetnext -v {{version}} -c {{community}} -O f {{ip_address}} {{oid}}`

- Ցուցադրել օգնությունը.:

`snmpgetnext {{[-h|--help]}}`
