# snmpgetnext

> MIB 트리에서 다음 값을 조회.
> 더 많은 정보: <https://manned.org/snmpgetnext>.

- SNMP 에이전트에서 다음 값 조회:

`snmpgetnext -v {{version}} -c {{커뮤니티}} {{ip_주소}} {{oid}}`

- 전체 Object Identifier (OID) 경로 표시:

`snmpgetnext -v {{version}} -c {{커뮤니티}} -O f {{ip_주소}} {{oid}}`

- 도움말 표시:

`snmpgetnext {{[-h|--help]}}`
