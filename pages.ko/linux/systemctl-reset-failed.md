# systemctl reset-failed

> 하나 이상 유닛의 "failed" 상태를 초기화.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#reset-failed%20%5BPATTERN%E2%80%A6%5D>.

- 모든 유닛의 실패 상태 초기화:

`systemctl reset-failed`

- 특정 유닛의 실패 상태 초기화:

`systemctl reset-failed {{유닛}}`

- 여러 유닛의 실패 상태를 한 번에 초기화:

`systemctl reset-failed {{유닛_1 유닛_2 ...}}`
