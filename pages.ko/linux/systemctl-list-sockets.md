# systemctl list-sockets

> 현재 메모리에 로드된 활성 socket 유닛을 리스닝 주소 기준으로 정렬하여 표시.
> 관련 항목: `systemctl list-units`, `systemctl list-unit-files`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-sockets%20PATTERN%E2%80%A6>.

- 현재 메모리에 있는 활성 socket 유닛 출력:

`systemctl list-sockets`

- socket 타입과 함께 활성 socket 유닛 출력:

`systemctl list-sockets --show-types`

- 비활성 및 실패한 유닛을 포함한 모든 socket 유닛 출력:

`systemctl list-sockets {{[-a|--all]}}`

- 상태 기준으로 socket 유닛 필터링:

`systemctl list-sockets --state {{active|inactive|failed|...}}`

- 이름 패턴으로 socket 유닛 필터링:

`systemctl list-sockets {{패턴1 패턴2 ...}}`
