# kodi-send

> Kodi에 액션 전송.
> 더 많은 정보: <https://kodi.wiki/view/List_of_built-in_functions>.

- Kodi 종료:

`kodi-send {{[-a|--action]}} Quit`

- 시스템 재부팅:

`kodi-send {{[-a|--action]}} Reboot`

- 원격 호스트 Kodi에 액션 전송:

`kodi-send --host {{192.168.0.1}} --port {{9777}} {{[-a|--action]}} {{Quit}}`
