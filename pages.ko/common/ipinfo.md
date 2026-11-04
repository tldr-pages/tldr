# ipinfo

> IPinfo.io의 IP 위치 정보 및 네트워크 인텔리전스 API를 위한 공식 CLI 도구.
> 참고: 일부 명령은 IPinfo.io 토큰이 필요.
> 더 많은 정보: <https://github.com/ipinfo/cli#quick-start>.

- 현재 IP 주소 정보 출력:

`ipinfo myip`

- 특정 IP 주소 정보 출력:

`ipinfo {{ip_주소}}`

- 파일의 여러 IP 주소를 일괄 조회:

`ipinfo bulk {{경로/대상/ips.txt}}`

- CIDR 또는 IP 범위 정보 조회:

`ipinfo bulk {{cidr_범위}}`

- IP lookup 결과 특정 필드만 출력:

`ipinfo {{ip_주소}} {{[-f|--field]}} {{hostname,country,org}}`

- 여러 IP 주소 요약 정보 출력:

`ipinfo summarize {{경로/대상/ips.txt}}`

- 텍스트에서 IP 주소 추출 및 강조:

`ipinfo grepip {{경로/대상/파일.txt}}`

- 도움말 표시:

`ipinfo {{[-h|--help]}}`
