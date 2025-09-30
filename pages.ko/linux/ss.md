# ss

> 소켓을 조사하는 유틸리티.
> 더 많은 정보: <https://manned.org/ss.8>.

- 모든 TCP/UDP/RAW/UNIX 소켓 표시:

`ss {{[-a|--all]}} {{-t|-u|-w|-x}}`

- 상태별로 TCP 소켓 필터링, 포함/제외:

`ss {{state|exclude}} {{bucket|big|connected|synchronized|...}}`

- 로컬 HTTPS 포트(443)에 연결된 모든 TCP 소켓 표시:

`ss {{[-t|--tcp]}} src :{{443}}`

- 로컬 8080 포트에서 수신 중인 모든 TCP 소켓 표시:

`ss {{[-lt|--listening --tcp]}} src :{{8080}}`

- 원격 SSH 포트에 연결된 프로세스와 함께 모든 TCP 소켓 표시:

`ss {{[-pt|--processes --tcp]}} dst :{{ssh}}`

- 특정 소스 및 목적지 포트에 연결된 모든 UDP 소켓 표시:

`ss {{[-u|--udp]}} 'sport == :{{소스_포트}} and dport == :{{목적지_포트}}'`

- 서브넷 192.168.0.0/16에 로컬로 연결된 모든 TCP IPv4 소켓 표시:

`ss {{[-4t|--ipv4 --tcp]}} src {{192.168/16}}`

- 목적지 IP 192.168.1.17 및 목적지 포트 8080의 IPv4 또는 IPv6 소켓 연결 종료:

`ss {{[-K|--kill]}} dst {{192.168.1.17}} dport = {{8080}}`
