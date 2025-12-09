# ipset

> 방화벽 규칙을 위한 IP 집합 생성.
> 더 많은 정보: <https://manned.org/ipset>.

- IP 주소를 포함할 빈 IP 집합 생성:

`ipset create {{집합_이름}} hash:ip`

- 특정 IP 집합 삭제:

`ipset destroy {{집합_이름}}`

- 특정 집합에 IP 주소 추가:

`ipset add {{집합_이름}} {{192.168.1.25}}`

- 집합에서 특정 IP 주소 삭제:

`ipset del {{집합_이름}} {{192.168.1.25}}`

- IP 집합 저장:

`ipset save {{집합_이름}} > {{경로/대상/ip_집합}}`
