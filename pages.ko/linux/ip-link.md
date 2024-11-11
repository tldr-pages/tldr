# ip link

> 네트워크 인터페이스 관리.
> 더 많은 정보: <https://manned.org/ip-link>.

- 모든 네트워크 인터페이스 정보 표시:

`ip link`

- 특정 네트워크 인터페이스 정보 표시:

`ip link show {{ethN}}`

- 네트워크 인터페이스 활성화 또는 비활성화:

`ip link set {{ethN}} {{up|down}}`

- 네트워크 인터페이스에 의미 있는 이름 부여:

`ip link set {{ethN}} alias "{{LAN 인터페이스}}"`

- 네트워크 인터페이스의 MAC 주소 변경:

`ip link set {{ethN}} address {{ff:ff:ff:ff:ff:ff}}`

- 네트워크 인터페이스의 MTU 크기를 변경하여 점보 프레임 사용:

`ip link set {{ethN}} mtu {{9000}}`
