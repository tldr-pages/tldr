# netstat

> 열린 연결 및 소켓 포트 등과 같은 네트워크 관련 정보를 표시합니다.
> 더 많은 정보: <https://man7.org/linux/man-pages/man8/netstat.8.html>.

- 모든 포트 나열:

`netstat --all`

- 모든 수신 포트 나열:

`netstat --listening`

- 수신 중인 TCP 포트 나열:

`netstat --tcp`

- PID 및 프로그램 이름 표시:

`netstat --program`

- 정보를 지속적으로 나열:

`netstat --continuous`

- 경로를 나열하고 IP 주소를 호스트 이름으로 확인하지 않음:

`netstat --route --numeric`

- 수신 TCP 및 UDP 포트 나열 (+ 루트인 경우 사용자 및 프로세스까지 포함):

`netstat --listening --program --numeric --tcp --udp --extend`
