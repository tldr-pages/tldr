# caffeinate

> macOS의 절전 모드를 방지합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- 1시간(3600초) 동안 절전 모드 방지:

`caffeinate -u -t {{3600}}`

- 명령이 완료될 때까지 절전 모드 방지:

`caffeinate -s "{{명령}}"`

- 지정된 PID를 가진 프로세스가 완료될 때까지 절전 모드 방지:

`caffeinate -w {{PID}}`

- 절전 모드 방지 (`<Ctrl c>`로 종료):

`caffeinate -i`

- 모니터 꺼짐 방지 (`<Ctrl c>`로 종료):

`caffeinate -d`

- 디스크 절전 모드 방지 (`<Ctrl c>`로 종료):

`caffeinate -m`
