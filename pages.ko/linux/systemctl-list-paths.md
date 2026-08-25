# systemctl list-paths

> 현재 메모리에 로드된 path 유닛을, 경로 기준으로 정렬하여 표시함.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-paths%20PATTERN%E2%80%A6>.

- 현재 메모리에 있는 모든 path 유닛 출력:

`systemctl list-paths`

- 특정 와일드카드 패턴(즉, `shell-globbing`)과 일치하는 path 유닛 출력:

`systemctl list-paths {{패턴}}`

- 여러 패턴과 일치하는 path 유닛 출력:

`systemctl list-paths {{패턴_1 패턴_2 ...}}`

- 비활성 유닛을 포함한 모든 path 유닛 출력:

`systemctl list-paths {{[-a|--all]}}`

- 상태 기준으로 path 유닛 필터링:

`systemctl list-paths --state {{상태}}`

- 출력에 유닛 타입도 함께 표시:

`systemctl list-paths --show-types`
