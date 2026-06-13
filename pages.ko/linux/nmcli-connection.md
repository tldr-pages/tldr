# nmcli connection

> NetworkManager와 함께 연결 관리.
> 더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#connection>.

- 모든 NetworkManager 연결 나열(이름, UUID, 유형 및 장치 표시):

`nmcli {{[c|connection]}}`

- 연결 활성화:

`nmcli {{[c|connection]}} {{[u|up]}} {{uuid}}`

- 연결 비활성화:

`nmcli {{[c|connection]}} {{[d|down]}} {{uuid}}`

- 자동 구성된 듀얼 스택 연결 생성:

`nmcli {{[c|connection]}} {{[a|add]}} ifname {{인터페이스_이름}} type {{이더넷}} ipv4.method {{auto}} ipv6.method {{auto}}`

- 고정 IPv6 전용 연결 생성:

`nmcli {{[c|connection]}} {{[a|add]}} ifname {{인터페이스_이름}} type {{이더넷}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- 고정 IPv4 전용 연결 생성:

`nmcli {{[c|connection]}} {{[a|add]}} ifname {{인터페이스_이름}} type {{이더넷}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`

- OVPN 파일에서 OpenVPN을 사용하여 VPN 연결 생성:

`nmcli {{[c|connection]}} {{[i|import]}} type {{openvpn}} file {{경로/대상/vpn_구성.ovpn}}`
