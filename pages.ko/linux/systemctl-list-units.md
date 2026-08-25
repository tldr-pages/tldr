# systemctl list-units

> systemd가 현재 메모리에 로드하고 있는 유닛을 나열.
> 관련 항목: `systemctl list-unit-files`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-units%20PATTERN%E2%80%A6>.

- 활성 상태이거나, 작업이 대기 중이거나, 실패한 유닛 목록 출력:

`systemctl list-units`

- 비활성 유닛을 포함한 모든 유닛 출력:

`systemctl list-units {{[-a|--all]}}`

- 유닛 타입 기준으로 필터링:

`systemctl list-units {{[-t|--type]}} {{service|socket|timer|...}}`

- 상태를 기준으로 필터링:

`systemctl list-units --state {{running|listening|dead|...}}`

- 이름 기준으로 필터링:

`systemctl list-units 'systemd*'`

- 페이저 없이 `stdout`으로 출력:

`systemctl list-units --no-pager`

- 헤더 및 푸터 없이 출력 (스크립트용):

`systemctl list-units --no-legend`
