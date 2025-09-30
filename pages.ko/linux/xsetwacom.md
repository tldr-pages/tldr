# xsetwacom

> 커맨드 라인 도구로, Wacom 펜 태블릿의 설정을 실행 중에 변경합니다.
> 더 많은 정보: <https://manned.org/xsetwacom>.

- 사용 가능한 모든 Wacom 장치를 나열. 장치 이름은 첫 번째 열에 표시됩니다:

`xsetwacom list`

- Wacom 영역을 특정 화면에 설정. 화면 이름은 `xrandr`로 확인:

`xsetwacom set "{{장치_이름}}" MapToOutput {{화면}}`

- 모드를 상대적(마우스처럼) 또는 절대적(펜처럼) 모드로 설정:

`xsetwacom set "{{장치_이름}}" Mode "{{Relative|Absolute}}"`

- 입력을 회전(화면을 회전할 때 유용) "자연" 회전에서 0|90|180|270 도로 설정:

`xsetwacom set "{{장치_이름}}" Rotate {{none|half|cw|ccw}}`

- 펜촉이 태블릿에 닿을 때만 버튼이 작동하도록 설정:

`xsetwacom set "{{장치_이름}}" TabletPCButton "on"`
