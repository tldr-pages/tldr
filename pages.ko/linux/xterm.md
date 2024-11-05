# xterm

> X 윈도우 시스템용 터미널 에뮬레이터.
> 더 많은 정보: <https://manned.org/xterm>.

- `Example`이라는 제목으로 터미널 열기:

`xterm -T {{Example}}`

- 전체 화면 모드로 터미널 열기:

`xterm -fullscreen`

- 어두운 파란색 배경과 노란색 전경(글꼴 색상)으로 터미널 열기:

`xterm -bg {{darkblue}} -fg {{yellow}}`

- 각 줄에 100자, 35줄로, 화면 위치 x=200px, y=20px에 터미널 열기:

`xterm -geometry {{100}}x{{35}}+{{200}}+{{20}}`

- Serif 글꼴과 글꼴 크기 20으로 터미널 열기:

`xterm -fa {{'Serif'}} -fs {{20}}`
