# gpclient

> OpenConnect를 통해 Linux에서 GlobalProtect VPN에 연결.
> 더 많은 정보: <https://github.com/yuezk/GlobalProtect-openconnect>.

- 포털 서버를 사용하여 GlobalProtect VPN에 연결:

`gpclient connect {{vpn_게이트웨이_URL}}`

- 현재 연결된 VPN 서버에서 연결 해제:

`gpclient disconnect`

- VPN 관리를 위한 그래픽 사용자 인터페이스(GUI) 실행:

`gpclient launch-gui`

- OpenSSL 우회 방법을 사용하여 레거시 재협상 오류 우회:

`gpclient connect --fix-openssl {{vpn_게이트웨이_URL}}`

- 연결 중 TLS 오류 무시:

`gpclient connect --ignore-tls-errors {{vpn_게이트웨이_URL}}`

- 버전 표시:

`gpclient --version`

- 명령에 대한 도움말 표시:

`gpclient help {{명령}}`
