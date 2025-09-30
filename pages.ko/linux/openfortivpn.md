# openfortivpn

> Fortinet의 독점 PPP+SSL VPN 솔루션을 위한 VPN 클라이언트.
> 더 많은 정보: <https://manned.org/openfortivpn>.

- 사용자명과 비밀번호로 VPN에 연결:

`openfortivpn {{[-u|--username]}} {{사용자명}} {{[-p|--password]}} {{비밀번호}}`

- 특정 구성 파일을 사용하여 VPN에 연결 (`/etc/openfortivpn/config`가 기본값):

`sudo openfortivpn {{[-c|--config]}} {{경로/대상/구성}}`

- 호스트와 포트를 지정하여 VPN에 연결:

`openfortivpn {{호스트}}:{{포트}}`

- 인증서의 sha256 합계를 전달하여 특정 게이트웨이를 신뢰:

`openfortivpn --trusted-cert {{sha256_합계}}`
