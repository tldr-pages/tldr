# openconnect

> Cisco AnyConnect VPN 및 기타 VPN을 위한 VPN 클라이언트.
> 더 많은 정보: <https://www.infradead.org/openconnect/manual.html>.

- 서버에 연결:

`openconnect {{vpn.example.org}}`

- 백그라운드에서 실행되도록 서버에 연결:

`openconnect --background {{vpn.example.org}}`

- 백그라운드에서 실행 중인 연결 종료:

`killall -SIGINT openconnect`

- 설정 파일에서 옵션을 읽어 서버에 연결:

`openconnect --config={{경로/대상/파일}} {{vpn.example.org}}`

- 특정 SSL 클라이언트 인증서로 인증하여 서버에 연결:

`openconnect --certificate={{경로/대상/파일}} {{vpn.example.org}}`
