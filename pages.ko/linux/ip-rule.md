# ip rule

> IP 라우팅 정책 데이터베이스 관리.
> 더 많은 정보: <https://manned.org/ip-rule>.

- 라우팅 정책 표시:

`ip rule {{show|list}}`

- 패킷 소스 주소를 기준으로 새 규칙 추가:

`sudo ip rule add from {{192.168.178.2/32}}`

- 패킷 목적지 주소를 기준으로 새 규칙 추가:

`sudo ip rule add to {{192.168.178.2/32}}`

- 패킷 소스 주소를 기준으로 규칙 삭제:

`sudo ip rule delete from {{192.168.178.2/32}}`

- 패킷 목적지 주소를 기준으로 규칙 삭제:

`sudo ip rule delete to {{192.168.178.2/32}}`

- 삭제된 모든 규칙 플러시:

`ip rule flush`

- 모든 규칙을 파일에 저장:

`ip rule save > {{경로/대상/ip_규칙들.dat}}`

- 파일에서 모든 규칙 복원:

`ip rule restore < {{경로/대상/ip_규칙들.dat}}`
