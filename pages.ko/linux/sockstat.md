# sockstat

> 열린 인터넷 또는 UNIX 도메인 소켓 나열.
> 같이 보기: `netstat`.
> 더 많은 정보: <https://manned.org/sockstat>.

- 대기 중이거나 연결된 IPv4 및 IPv6 소켓 정보 표시:

`sockstat`

- 특정 프로토콜을 사용하여 특정 포트에서 [l]대기 중인 IPv[4]/IPv[6] 소켓 정보 표시:

`sockstat -{{4|6}} -l -R {{tcp|udp|raw|unix}} -p {{포트1,포트2...}}`

- [c]연결된 소켓 및 [u]유닉스 소켓도 표시:

`sockstat -cu`

- 지정된 `pid` 또는 프로세스의 소켓만 표시:

`sockstat -P {{pid|프로세스}}`

- 지정된 `uid` 또는 사용자의 소켓만 표시:

`sockstat -U {{uid|사용자}}`

- 지정된 `gid` 또는 그룹의 소켓만 표시:

`sockstat -G {{gid|그룹}}`
