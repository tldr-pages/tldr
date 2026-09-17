# systemctl help

> 하나 이상의 유닛 또는 특정 PID에 해당하는 유닛의 사용 설명 페이지를 표시.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#help%20PATTERN%E2%80%A6%7CPID%E2%80%A6>.

- 특정 유닛의 사용 설명 페이지 출력:

`systemctl help {{유닛}}`

- 여러 유닛의 사용 설명 페이지 출력:

`systemctl help {{유닛1 유닛2 ...}}`

- 사용자 유닛의 사용 설명 페이지 출력:

`systemctl help {{유닛}} --user`

- 페이저 없이 전체 사용 설명 페이지 출력:

`systemctl help {{유닛}} --no-pager`

- 특정 PID가 속한 유닛의 사용 설명 페이지 출력:

`systemctl help {{pid}}`
