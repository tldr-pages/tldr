# systemctl suspend

> 시스템을 절전 모드로 전환.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#suspend>.

- 즉시 절전 모드로 전환:

`systemctl suspend`

- 5분 후 절전 모드로 전환:

`sleep 300 && systemctl suspend`

- 절전 후 일정 시간 뒤 최대 절전으로 전환:

`systemctl hybrid-sleep`
