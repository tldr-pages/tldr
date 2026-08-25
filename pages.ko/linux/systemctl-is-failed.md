# systemctl is-failed

> 하나 이상의 systemd 유닛이 실패 상태인지 확인.
> 관련 항목: `systemctl is-active`, `systemctl status`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-failed%20PATTERN%E2%80%A6>.

- 실패한 유닛이 있는지 확인:

`systemctl is-failed`

- 특정 유닛 또는 여러 유닛의 실패 여부 확인:

`systemctl is-failed {{유닛1 유닛2 ...}}`

- 출력 없이 종료 코드로만 확인:

`systemctl is-failed {{유닛}} {{[-q|--quiet]}}`

- 사용자 유닛의 실패 여부 확인:

`systemctl is-failed {{유닛}} --user`
