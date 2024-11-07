# picom-trans

> `picom` 윈도우 합성기의 윈도우 투명도를 설정.
> 더 많은 정보: <https://github.com/yshui/picom>.

- 현재 포커스된 윈도우의 투명도를 특정 퍼센트로 설정:

`picom-trans --current --opacity {{90}}`

- 특정 이름을 가진 윈도우의 투명도를 설정:

`picom-trans --name {{Firefox}} --opacity {{90}}`

- 마우스 커서로 선택한 특정 윈도우의 투명도를 설정:

`picom-trans --select --opacity {{90}}`

- 특정 윈도우의 투명도를 토글:

`picom-trans --name {{Firefox}} --toggle`
