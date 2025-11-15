# wtype

> Wayland에서 키보드 입력을 시뮬레이트합니다. X11의 `xdotool type`과 유사합니다.
> 같이 보기: `ydotool`.
> 더 많은 정보: <https://manned.org/wtype>.

- 텍스트 입력을 시뮬레이트:

`wtype "{{Hello World}}"`

- 특정 키 입력:

`wtype -k {{Left}}`

- 수정 키 누르기:

`wtype -M {{shift|ctrl|...}}`

- 수정 키 놓기:

`wtype -m {{ctrl}}`

- 키 입력 간 대기 시간 설정 (밀리초):

`wtype -d {{500}} -- "{{텍스트}}"`

- `stdin`에서 텍스트 읽기:

`echo "{{텍스트}}" | wtype -`
