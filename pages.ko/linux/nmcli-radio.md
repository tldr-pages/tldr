# nmcli radio

> 라디오 스위치의 상태를 표시하거나 NetworkManager를 사용하여 활성화/비활성화.
> 이 하위 명령은 `nmcli r`로도 호출할 수 있습니다.
> 더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#radio>.

- Wi-Fi 상태 표시:

`nmcli radio wifi`

- Wi-Fi 켜기 또는 끄기:

`nmcli radio wifi {{on|off}}`

- WWAN 상태 표시:

`nmcli radio wwan`

- WWAN 켜기 또는 끄기:

`nmcli radio wwan {{on|off}}`

- 두 스위치의 상태 표시:

`nmcli radio all`

- 두 스위치 켜기 또는 끄기:

`nmcli radio all {{on|off}}`
