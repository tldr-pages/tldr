# uvcdynctrl

> uvcvideo에서 동적 제어를 관리하는 libwebcam 명령줄 도구.
> 더 많은 정보: <https://manned.org/uvcdynctrl>.

- 사용 가능한 모든 카메라 나열:

`uvcdynctrl -l`

- 특정 디바이스 사용 (`video0`이 기본값):

`uvcdynctrl -d {{디바이스_이름}}`

- 사용 가능한 제어 목록 나열:

`uvcdynctrl -c`

- 새로운 제어 값 설정 (음수 값을 위해서는 `-- -값` 사용):

`uvcdynctrl -s {{제어_이름}} {{값}}`

- 현재 제어 값 가져오기:

`uvcdynctrl -g {{제어_이름}}`

- 현재 제어 상태를 파일에 저장:

`uvcdynctrl -W {{파일명}}`

- 파일에서 제어 상태 로드:

`uvcdynctrl -L {{파일명}}`
