# systemctl suspend-then-hibernate

> 시스템을 절전 상태로 전환한 뒤, 일정 시간 비활성 상태가 지속되면 자동으로 최대 절전 상태로 전환.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#suspend-then-hibernate>.

- 설정된 지연 시간 후 최대 절전으로 전환:

`systemctl suspend-then-hibernate`

- inhibitor 잠금을 무시하고 강제로 suspend-then-hibernate 실행:

`systemctl suspend-then-hibernate {{[-f|--force]}}`
