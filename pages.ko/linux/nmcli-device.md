# nmcli device

> NetworkManager를 사용하여 네트워크 인터페이스를 관리하고 새로운 Wi-Fi 연결을 설정합니다.
> 이 하위 명령은 `nmcli d`로도 호출할 수 있습니다.
> 더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#device>.

- 모든 네트워크 인터페이스의 상태를 출력:

`nmcli device status`

- 사용 가능한 Wi-Fi 액세스 포인트를 출력:

`nmcli device wifi`

- 지정된 SSID의 Wi-Fi 네트워크에 연결 (비밀번호 입력 요청이 표시됨):

`nmcli --ask device wifi connect {{ssid}}`

- 현재 Wi-Fi 네트워크의 비밀번호와 QR 코드를 출력:

`nmcli device wifi show-password`
