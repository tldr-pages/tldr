# netstat

> 네트워크 관련 정보(열려 있는 연결, 소켓 포트 등) 표시.
> 관련 항목: `ss`.
> 더 많은 정보: <https://manned.org/netstat>.

- 모든 포트 나열:

`netstat {{[-a|--all]}}`

- 수신 대기 중인 모든 포트 나열:

`netstat {{[-l|--listening]}}`

- 수신 대기 중인 TCP 포트 나열:

`netstat {{[-t|--tcp]}}`

- PID 및 프로그램 이름 표시:

`netstat {{[-p|--program]}}`

- 정보를 지속적으로 나열:

`netstat {{[-c|--continuous]}}`

- 경로를 나열하고 IP 주소를 호스트 이름으로 변환하지 않음:

`netstat {{[-rn|--route --numeric]}}`

- 수신 대기 중인 TCP 및 UDP 포트 나열 (+ 루트 권한일 경우 사용자 및 프로세스 표시):

`netstat {{[-tulpne|--tcp --udp --listening --program --numeric --extend]}}`
