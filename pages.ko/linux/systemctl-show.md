# systemctl show

> 유닛 또는 systemd 자체의 속성을 출력.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#show%20PATTERN%E2%80%A6%7CJOB%E2%80%A6>.

- 시스템 서비스 매니저의 속성 출력:

`systemctl show`

- 사용자 서비스 매니저의 속성 출력:

`systemctl show --user`

- 특정 유닛의 속성 출력:

`systemctl show {{unit}}`

- 특정 사용자 유닛의 속성 출력:

`systemctl show {{unit}} --user`

- 빈 속성까지 포함하여 출력:

`systemctl show {{[-a|--all]}}`

- 지정한 속성만 출력:

`systemctl show {{unit}} {{[-p|--property]}} {{Wants,Conflicts,...}}`
