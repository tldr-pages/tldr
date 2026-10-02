# snmpget

> SNMP 프로토콜을 사용해 값을 조회.
> 더 많은 정보: <https://manned.org/snmpget>.

- SNMP 에이전트에서 단일 값 조회:

`snmpget -v {{버전}} -c {{커뮤니티}} {{ip_주소}} {{oid}}`

- 전체 Object Identifier (OID) 경로 표시:

`snmpget -v {{버전}} -c {{커뮤니티}} -O f {{ip_address}} {{oid}}`

- 도움말 표시:

`snmpget {{[-h|--help]}}`
