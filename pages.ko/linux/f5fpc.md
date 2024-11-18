# f5fpc

> BIG-IP Edge의 독점 상업용 SSL VPN 클라이언트.
> 더 많은 정보: <https://techdocs.f5.com/kb/en-us/products/big-ip_apm/manuals/product/apm-client-configuration-11-4-0/4.html>.

- 새 VPN 연결 열기:

`sudo f5fpc --start`

- 특정 호스트에 새 VPN 연결 열기:

`sudo f5fpc --start --host {{host.example.com}}`

- 사용자명 지정 (암호는 사용자에게 요청됨):

`sudo f5fpc --start --host {{host.example.com}} --username {{사용자}}`

- 현재 VPN 상태 표시:

`sudo f5fpc --info`

- VPN 연결 종료:

`sudo f5fpc --stop`
