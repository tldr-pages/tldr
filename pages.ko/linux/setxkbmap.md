# setxkbmap

> X Keyboard Extension을 사용하여 키보드를 설정합니다.
> 더 많은 정보: <https://manned.org/setxkbmap>.

- 키보드를 프랑스어 AZERTY로 설정:

`setxkbmap {{fr}}`

- 여러 키보드 레이아웃, 변형 및 전환 옵션 설정:

`setxkbmap -layout {{us,de}} -variant {{,qwerty}} -option {{'grp:alt_caps_toggle'}}`

- 도움말 보기:

`setxkbmap -help`

- 모든 레이아웃 나열:

`localectl list-x11-keymap-layouts`

- 레이아웃의 변형 나열:

`localectl list-x11-keymap-variants {{de}}`

- 사용 가능한 전환 옵션 나열:

`localectl list-x11-keymap-options | grep grp:`
