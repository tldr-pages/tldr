# zmap

> 인터넷 규모의 네트워크 분석을 위한 빠른 오픈소스 스캐너.
> 관련 항목: `hping3`, `masscan`, `naabu`, `nmap`, `rustscan`.
> 더 많은 정보: <https://manned.org/zmap>.

- 특정 TCP 포트 (기본값: 80)에 대해 서브넷 또는 전체 IPv4 스캔:

`zmap {{서브넷}} {{[-p|--target-ports]}} {{port}}`

- 서브넷 전체에 대해 특정 포트 또는 포트 범위 스캔:

`zmap {{[-p|--target-ports]}} {{포트1,포트2-포트3,...}} {{서브넷}}`

- 사용자 정의 필드로 CSV 파일에 결과 출력:

`zmap {{[-o|--output-file]}} {{경로/대상/출력_파일.csv}} {{[-f|--output-fields]}} "{{saddr,daddr,sport,dport}}" {{서브넷}}`

- 초당 패킷 수를 제한하여 스캔 속도 조절:

`zmap {{[-r|--rate]}} {{초당_패킷}} {{서브넷}}`

- 실제 패킷 전송 없이 시뮬레이션 실행:

`zmap {{[-d|--dryrun]}} {{서브넷}}`

- CIDR 형식의 blocklist 파일로 특정 서브넷 제외:

`zmap {{[-b|--blocklist-file]}} {{경로/대상/blocklist.txt}} {{서브넷}}`

- 스캔 패킷에 사용할 소스 IP 지정:

`zmap {{[-S|--source-ip]}} {{소스_ip}} {{서브넷}}`

- 스캔 대상 수/비율 제한 (예: 1000개 IP/포트 조합):

`zmap {{[-n|--max-targets]}} {{1000}} {{서브넷}} {{[-p|--target-ports]}} {{포트1,포트2-포트3}}`
