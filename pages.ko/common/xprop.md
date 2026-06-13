# xprop

> X 서버에서 창 및 폰트 속성을 표시.
> 더 많은 정보: <https://manned.org/xprop>.

- 루트 창의 이름 표시:

`xprop -root WM_NAME`

- 창의 윈도우 매니저 힌트 표시:

`xprop -name "{{창_이름}}" WM_HINTS`

- 폰트의 포인트 크기 표시:

`xprop -font "{{폰트_이름}}" POINT_SIZE`

- ID가 0x200007인 창의 모든 속성 표시:

`xprop -id {{0x200007}}`
