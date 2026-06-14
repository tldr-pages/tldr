# snmpget

> Հարցում` օգտագործելով SNMP արձանագրությունը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/snmpget>:.

- SNMP գործակալից պահանջեք մեկ արժեք.:

`snmpget -v {{version}} -c {{community}} {{ip_address}} {{oid}}`

- Ցուցադրել օբյեկտի նույնացուցիչի (OID) ամբողջական ուղին.:

`snmpget -v {{version}} -c {{community}} -O f {{ip_address}} {{oid}}`

- Ցուցադրել օգնությունը.:

`snmpget {{[-h|--help]}}`
