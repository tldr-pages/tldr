# snmpbulkget

> MIB 트리에서 다음 값과 그 인접한 값들을 조회.
> 더 많은 정보: <https://manned.org/snmpbulkget>.

- SNMP 에이전트에서 다음 값을 요청:

`snmpbulkget -v {{버전}} -c {{커뮤니티}} {{ip_주소}} {{oid}}`

- 전체 OID(Object Identifier) 경로를 표시:

`snmpbulkget -v {{버전}} -c {{커뮤니티}} -O f {{ip_주소}} {{oid}}`

- 도움말 표시:

`snmpbulkget {{[-h|--help]}}`
