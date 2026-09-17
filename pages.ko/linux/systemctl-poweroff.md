# systemctl-poweroff

> 시스템 전원을 종료.
> 관련 항목: `poweroff`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#poweroff>.

- 시스템 전원 종료:

`systemctl poweroff`

- 서비스 종료 절차 없이 즉시 전원 종료:

`systemctl poweroff {{[-f|--force]}}`

- 로그인 사용자에게 알림 없이 즉시 전원 종료:

`systemctl poweroff {{[-f|--force]}} --no-wall`
