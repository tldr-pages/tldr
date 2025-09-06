# shutdown

> 시스템을 종료하고 재부팅합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/shutdown.8.html>.

- 즉시 시스템 전원 끄기 (정지):

`shutdown -h now`

- 즉시 절전 모드로 전환:

`shutdown -s now`

- 즉시 재부팅:

`shutdown -r now`

- 5분 후 재부팅:

`shutdown -r "+{{5}}"`

- 오후 1시에 시스템 전원 끄기 (24시간 형식 사용):

`shutdown -h {{1300}}`

- 2042년 5월 10일 오전 11시 30분에 재부팅 (입력 형식: YYMMDDHHMM):

`shutdown -r {{4205101130}}`
