# ip route get

> 목적지로 가는 단일 경로를 가져와 커널이 인식하는 그대로 내용을 출력합니다.
> 더 많은 정보: <https://manned.org/ip-route>.

- 목적지로 가는 경로 출력:

`ip route get {{1.1.1.1}}`

- 특정 소스 주소에서 목적지로 가는 경로 출력:

`ip route get {{목적지}} from {{소스}}`

- 특정 인터페이스를 통해 도착하는 패킷의 목적지로 가는 경로 출력:

`ip route get {{목적지}} iif {{eth0}}`

- 특정 인터페이스를 통해 강제로 출력하는 목적지로 가는 경로 출력:

`ip route get {{목적지}} oif {{eth1}}`

- 지정된 서비스 유형(ToS)으로 목적지로 가는 경로 출력:

`ip route get {{목적지}} tos {{0x10}}`

- 특정 VRF(가상 라우팅 및 전달) 인스턴스를 사용하여 목적지로 가는 경로 출력:

`ip route get {{목적지}} vrf {{myvrf}}`
