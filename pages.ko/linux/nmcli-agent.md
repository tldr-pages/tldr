# nmcli agent

> `nmcli`를 NetworkManager 비밀 요원이나 polkit 요원으로 실행.
> 더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#agent>.

- `nmcli`를 비밀 요원으로 등록하고 비밀 요청 수신 대기:

`nmcli {{[a|agent]}} {{[s|secret]}}`

- `nmcli`를 polkit 요원으로 등록하고 권한 요청 수신 대기:

`nmcli {{[a|agent]}} {{[p|polkit]}}`

- `nmcli`를 비밀 요원 및 polkit 요원으로 등록:

`nmcli {{[a|agent]}} {{[a|all]}}`
