# systemctl list-timers

> 현재 활성화된 모든 systemd 타이머를 표시.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-timers%20PATTERN%E2%80%A6>.

- 모든 활성 타이머 출력:

`systemctl list-timers`

- 비활성 타이머를 포함한 모든 타이머 출력:

`systemctl list-timers {{[-a|--all]}}`

- 특정 패턴과 일치하는 타이머 출력:

`systemctl list-timers {{패턴}}`

- 특정 상태의 타이머만 출력:

`systemctl list-timers --state {{active|inactive|failed|...}}`
