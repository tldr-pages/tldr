# ip

> 라우팅, 디바이스, 정책 라우팅 및 터널을 표시/조작.
> `address`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://www.manned.org/ip.8>.

- 인터페이스를 자세한 정보와 함께 나열:

`ip address`

- 네트워크 계층 정보 요약과 함께 인터페이스 나열:

`ip -brief address`

- 링크 계층 정보 요약과 함께 인터페이스 나열:

`ip -brief link`

- 라우팅 테이블 표시:

`ip route`

- 이웃(ARP 테이블) 표시:

`ip neighbour`

- 인터페이스를 활성화/비활성화:

`ip link set {{인터페이스}} {{up|down}}`

- 인터페이스에 IP 주소 추가/삭제:

`ip addr add/del {{IP}}/{{마스크}} dev {{인터페이스}}`

- 기본 경로 추가:

`ip route add default via {{IP}} dev {{인터페이스}}`
