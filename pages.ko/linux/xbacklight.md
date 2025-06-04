# xbacklight

> RandR 확장을 사용하여 화면 밝기를 조절하는 유틸리티.
> 더 많은 정보: <https://manned.org/xbacklight>.

- 현재 화면 밝기를 퍼센트로 확인:

`xbacklight`

- 화면 밝기를 40%로 설정:

`xbacklight -set {{40}}`

- 현재 밝기를 25% 증가:

`xbacklight -inc {{25}}`

- 현재 밝기를 75% 감소:

`xbacklight -dec {{75}}`

- 60초(밀리초 단위) 동안 60단계로 화면 밝기를 100%로 증가:

`xbacklight -set {{100}} -time {{60000}} -steps {{60}}`
