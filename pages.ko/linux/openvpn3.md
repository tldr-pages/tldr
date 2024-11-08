# openvpn3

> OpenVPN 3 Linux 클라이언트.
> 더 많은 정보: <https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>.

- 새 VPN 세션 시작:

`openvpn3 session-start --config {{경로/대상/config.conf}}`

- 설정된 세션 나열:

`openvpn3 sessions-list`

- 주어진 구성으로 시작된 현재 설정된 세션 연결 해제:

`openvpn3 session-manage --config {{경로/대상/config.conf}} --disconnect`

- VPN 구성 가져오기:

`openvpn3 config-import --config {{경로/대상/config.conf}}`

- 가져온 구성 나열:

`openvpn3 configs-list`
