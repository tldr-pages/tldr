# tty-clock

> 사용자 지정 가능한 터미널 기반 디지털 시계.
> 더 많은 정보: <https://github.com/xorg62/tty-clock>.

- 터미널 중앙에서 시계 시작:

`tty-clock -c`

- 초 표시 활성화:

`tty-clock -s`

- 색상 코드 (0-7)를 사용해 시계 색상 설정:

`tty-clock -C {{color_number}}`

- 사용자 지정 날짜 형식 (strftime 형식) 사용:

`tty-clock -f "{{%A, %B %d}}"`

- 새로 고침 간격(초) 설정 (기본값: 1):

`tty-clock -d {{초}}`

- 실행 중인 시계 종료:

`<q>`
