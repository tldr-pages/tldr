# nmcli networking

> NetworkManager의 네트워킹 상태를 관리합니다.
> 이 하위 명령은 `nmcli n`으로도 호출할 수 있습니다.
> 더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#networking>.

- NetworkManager의 네트워킹 상태 표시:

`nmcli networking`

- NetworkManager가 관리하는 네트워킹 및 모든 인터페이스 활성화 또는 비활성화:

`nmcli networking {{on|off}}`

- 마지막으로 알려진 연결 상태 표시:

`nmcli networking connectivity`

- 현재 연결 상태 확인:

`nmcli networking connectivity check`
