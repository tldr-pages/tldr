# systemctl status

> systemd 유닛의 상태를 출력.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#status%20PATTERN%E2%80%A6%7CPID%E2%80%A6%5D>.

- 특정 systemd 유닛의 상태 출력:

`systemctl status {{유닛}}.{{service|timer|socket|target|...}}`

- 실패한 유닛 상태 출력:

`systemctl status --failed`

- 실행 중인 모든 서비스 목록 출력:

`systemctl status`

- 시스템의 모든 유닛 출력:

`systemctl status {{[-a|--all]}}`

- 특정 타입의 유닛만 출력:

`systemctl status {{[-t|--type]}} {{service|timer|socket|target|...}}`

- 특정 상태의 유닛만 출력:

`systemctl status --state {{active|inactive|failed}}`

- 사용자 유닛 상태 출력:

`systemctl status {{유닛}} --user`
