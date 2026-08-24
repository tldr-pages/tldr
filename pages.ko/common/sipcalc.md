# sipcalc

> IPv4 및 IPv6 주소의 IP 서브넷 정보를 계산.
> 관련 항목: `ipcalc`.
> 더 많은 정보: <https://manned.org/sipcalc>.

- IPv4 CIDR 주소의 서브넷 정보를 표시:

`sipcalc {{192.168.1.0/24}}`

- 주소에 대한 모든 정보 표시:

`sipcalc {{[-a|--all]}} {{192.168.1.0/24}}`

- 지정한 서브넷 마스크로 IPv4 네트워크를 분할:

`sipcalc {{[-s|--v4split]}} {{255.255.255.128}} {{192.168.1.0/24}}`

- IPv6 역방향 DNS 정보를 표시:

`sipcalc {{[-r|--v6rev]}} {{2001:db8::/32}}`

- DNS 이름 확인을 활성화:

`sipcalc {{[-d|--resolve]}} {{192.168.1.0/24}}`

- 도움말 표시:

`sipcalc {{[-h|--help]}}`
