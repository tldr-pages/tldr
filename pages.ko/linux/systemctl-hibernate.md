# systemctl hibernate

> 현재 상태를 디스크에 저장한 뒤, 시스템 전원을 끄는 최대 절전 모드로 전환.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#hibernate>.

- 즉시 최대 절전 모드로 전환:

`systemctl hibernate`

- inhibitors가 있어도 강제로 최대 절전 모드로 전환:

`systemctl hibernate {{[-f|--force]}}`

- 로그인 사용자에게 알림 없이 최대 절전 모드로 전환:

`systemctl hibernate --no-wall`
