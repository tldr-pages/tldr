# nmcli radio

> 라디오 스위치의 상태를 표시하거나 NetworkManager를 사용하여 활성화/비활성화.
> 더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#radio>.

- Wi-Fi 상태 표시:

`nmcli {{[r|radio]}} {{[w|wifi]}}`

- Wi-Fi 켜기 또는 끄기:

`nmcli {{[r|radio]}} {{[w|wifi]}} {{on|off}}`

- WWAN 상태 표시:

`nmcli {{[r|radio]}} {{[ww|wwan]}}`

- WWAN 켜기 또는 끄기:

`nmcli {{[r|radio]}} {{[ww|wwan]}} {{on|off}}`

- 두 스위치의 상태 표시:

`nmcli {{[r|radio]}}`

- 두 스위치 켜기 또는 끄기:

`nmcli {{[r|radio]}} {{[a|all]}} {{on|off}}`
