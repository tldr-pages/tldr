# piactl

> 상업용 VPN 제공업체인 Private Internet Access의 명령줄 도구.
> 더 많은 정보: <https://helpdesk.privateinternetaccess.com/kb/articles/pia-desktop-command-line-interface-part-1>.

- Private Internet Access에 로그인:

`piactl login {{경로/대상/로그인_파일}}`

- Private Internet Access에 연결:

`piactl connect`

- Private Internet Access에서 연결 해제:

`piactl disconnect`

- 백그라운드에서 Private Internet Access 데몬 활성화 또는 비활성화:

`piactl background {{enable|disable}}`

- 사용 가능한 모든 VPN 지역 나열:

`piactl get regions`

- 현재 VPN 지역 표시:

`piactl get region`

- VPN 지역 설정:

`piactl set region {{지역}}`

- Private Internet Access에서 로그아웃:

`piactl logout`
