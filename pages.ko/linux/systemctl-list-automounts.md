# systemctl list-automounts

> 현재 메모리에 로드된 automount 유닛을 나열하며, 마운트 경로와 유닛 이름을 표시.
> 관련 항목: `systemctl list-units`, `systemctl list-unit-files`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-automounts%20PATTERN%E2%80%A6>.

- 현재 메모리에 있는 automount 유닛 목록 출력:

`systemctl list-automounts`

- 비활성 유닛을 포함한 모든 automount 유닛 목록 출력:

`systemctl list-automounts {{[-a|--all]}}`

- 상태 기준으로 automount 유닛 필터링:

`systemctl list-automounts --state {{active|inactive|failed|...}}`

- 이름 패턴으로 automount 유닛 필터링:

`systemctl list-automounts {{패턴1 패턴2 ...}}`
