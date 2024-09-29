# sockstat

> 열린 인터넷 또는 UNIX 도메인 소켓을 나열합니다.
> 참고: 이 프로그램은 FreeBSD의 `sockstat`를 NetBSD 3.0용으로 다시 작성한 것입니다.
> 같이 보기: `netstat`.
> 더 많은 정보: <https://man.netbsd.org/sockstat.1>.

- IPv4, IPv6 및 Unix 소켓에 대한 수신 및 연결된 소켓에 대한 정보 표시:

`sockstat`

- 특정 포트에서 특정 프로토콜을 사용하는 IPv[4]/IPv[6] 소켓 [l]istening에 대한 정보 표시:

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- [c]onnected 소켓도 표시하며 [u]nix 소켓도 표시:

`sockstat -cu`

- 주소 및 포트의 심볼릭 이름을 해결하지 않고 [n]umeric 출력만 표시:

`sockstat -n`

- 지정된 주소 [f]amily의 소켓만 나열:

`sockstat -f {{inet|inet6|local|unix}}`
