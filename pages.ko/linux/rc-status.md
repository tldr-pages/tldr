# rc-status

> runlevel의 상태 정보를 표시합니다.
> 관련 항목: `openrc`.
> 더 많은 정보: <https://manned.org/rc-status>.

- 서비스 및 해당 상태 요약 표시:

`rc-status`

- 모든 runlevel의 서비스를 요약에 포함:

`rc-status {{[-a|--all]}}`

- 충돌한 서비스 나열:

`rc-status {{[-c|--crashed]}}`

- 수동으로 시작된 서비스 나열:

`rc-status {{[-m|--manual]}}`

- 감독되는 서비스 나열:

`rc-status {{[-S|--supervised]}}`

- 현재 runlevel 얻기:

`rc-status {{[-r|--runlevel]}}`

- 모든 runlevel 나열:

`rc-status {{[-l|--list]}}`
