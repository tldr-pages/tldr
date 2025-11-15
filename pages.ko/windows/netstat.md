# netstat

> 활성 TCP 연결, 컴퓨터가 수신하는 포트, 네트워크 어댑터 통계, IP 라우팅 테이블, IPv4 통계 및 IPv6 통계를 표시합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/netstat>.

- 활성 TCP 연결 표시:

`netstat`

- 모든 활성 TCP 연결 및 컴퓨터가 수신 중인 TCP 및 UDP 포트 표시:

`netstat -a`

- 전송 및 수신된 바이트 및 패킷 수와 같은 네트워크 어댑터 통계를 표시:

`netstat -e`

- 활성 TCP 연결과 명시적 주소 및 포트 번호를 숫자로 표시:

`netstat -n`

- 활성 TCP 연결과 각 연결의 프로세스 ID(PID) 표시:

`netstat -o`

- IP 라우팅 테이블 내용 표시:

`netstat -r`

- 프로토콜별 통계 표시:

`netstat -s`

- 현재 열려 있는 포트 목록 및 관련 IP 주소 목록을 표시:

`netstat -an`
