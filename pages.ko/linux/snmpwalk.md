# snmpwalk

> SNMP 쿼리 도구.
> 더 많은 정보: <https://manned.org/snmpwalk>.

- SNMPv1과 커뮤니티 문자열을 사용하여 원격 호스트의 시스템 정보 쿼리:

`snmpwalk -v1 -c {{커뮤니티}} {{ip}}`

- SNMPv2를 사용하여 지정된 포트에서 OID로 원격 호스트의 시스템 정보 쿼리:

`snmpwalk -v2c -c {{커뮤니티}} {{ip}}:{{포트}} {{oid}}`

- SNMPv3과 인증(암호화 없이)을 사용하여 OID로 원격 호스트의 시스템 정보 쿼리:

`snmpwalk -v3 -l {{authNoPriv}} -u {{사용자명}} -a {{MD5|SHA}} -A {{암호}} {{ip}} {{oid}}`

- SNMPv3과 인증 및 암호화를 사용하여 OID로 원격 호스트의 시스템 정보 쿼리:

`snmpwalk -v3 -l {{authPriv}} -u {{사용자명}} -a {{MD5|SHA}} -A {{인증_암호}} -x {{DES|AES}} -X {{암호화_암호}} {{ip}} {{oid}}`

- SNMPv3을 사용하여 인증 또는 암호화 없이 OID로 원격 호스트의 시스템 정보 쿼리:

`snmpwalk -v3 -l {{noAuthNoPriv}} -u {{사용자명}} {{ip}} {{oid}}`
