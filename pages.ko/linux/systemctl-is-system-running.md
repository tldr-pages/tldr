# systemctl is-system-running

> 현재 시스템 상태를 확인.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-system-running>.

- 시스템이 정상적으로 동작 중인지 확인하고 현재 상태 출력:

`systemctl is-system-running`

- 현재 상태를 조용히 체크 및 출력 (출력 없이, 종료 상태로만 출력):

`systemctl is-system-running {{[-q|--quiet]}}`

- 부팅이 완료될 때까지 기다린 후 상태 출력:

`systemctl is-system-running --wait`
