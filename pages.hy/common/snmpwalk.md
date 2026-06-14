# snmpwalk

> SNMP հարցման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/snmpwalk>:.

- Հարցրեք հեռավոր հոսթի համակարգի տեղեկատվությունը SNMPv1-ի և համայնքի տողի միջոցով.:

`snmpwalk -v 1 -c {{community}} {{ip_address}}`

- Հարցման համակարգի տեղեկատվությունը հեռավոր հոսթի վրա OID-ի միջոցով՝ օգտագործելով SNMPv2 նշված նավահանգստում.:

`snmpwalk -v 2c -c {{community}} {{ip_address}}:{{port}} {{oid}}`

- Հարցրեք համակարգի տեղեկատվությունը հեռավոր հոսթի վրա OID-ի միջոցով՝ օգտագործելով SNMPv3 և նույնականացում առանց գաղտնագրման.:

`snmpwalk -v 3 -l {{authNoPriv}} -u {{username}} -a {{MD5|SHA}} -A {{passphrase}} {{ip_address}} {{oid}}`

- Հարցրեք համակարգի տեղեկատվությունը հեռավոր հոսթի վրա OID-ի միջոցով՝ օգտագործելով SNMPv3, իսկությունը և կոդավորումը.:

`snmpwalk -v 3 -l {{authPriv}} -u {{username}} -a {{MD5|SHA}} -A {{auth_passphrase}} -x {{DES|AES}} -X {{enc_passphrase}} {{ip_address}} {{oid}}`

- Հարցրեք համակարգի տեղեկատվությունը հեռավոր հոսթի վրա OID-ի միջոցով՝ օգտագործելով SNMPv3՝ առանց նույնականացման կամ գաղտնագրման.:

`snmpwalk -v 3 -l {{noAuthNoPriv}} -u {{username}} {{ip_address}} {{oid}}`

- Ցուցադրել օգնությունը.:

`snmpwalk {{[-h|--help]}}`
