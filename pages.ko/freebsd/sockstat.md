# sockstat

> 오픈된 인터넷 또는 UNIX 도메인 소켓을 나열합니다.
> 더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- 어떤 사용자/프로세스가 어떤 포트에서 [l]istening하는지 보기:

`sockstat -l`

- 특정 [p]ort에서 사용 중인 IPv[4]/IPv[6] 소켓 정보 보기, 특정 [P]rotocol 사용:

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- [c]onnected 소켓도 표시, 숫자형식의 UID를 사용자 이름으로 해석하지 않고 [w]ider 필드 크기 사용:

`sockstat -cnw`

- 특정 [j]ail ID 또는 이름에 속하는 소켓만 [v]erbose 모드로 표시:

`sockstat -jv`

- 프로토콜 [s]tate 및 원격 [U]DP 캡슐화 포트 번호 표시 (현재 SCTP 및 TCP에만 구현됨):

`sockstat -sU`

- [C]ongestion control 모듈 및 프로토콜 [S]tack 표시 (현재 TCP에만 구현됨):

`sockstat -CS`

- 로컬 및 외부 주소가 루프백 네트워크 접두어 127.0.0.0/8이 아니거나 IPv6 루프백 주소 ::1을 포함하지 않는 경우에만 인터넷 소켓 표시:

`sockstat -L`

- 헤더를 표시하지 않음 ([q]uiet 모드), [u]nix 소켓 표시하고 `inp_gencnt` 표시:

`sockstat -qui`
