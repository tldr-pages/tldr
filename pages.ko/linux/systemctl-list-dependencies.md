# systemctl list-dependencies

> systemd에서 유닛의 의존성 트리를 표시.
> 관련 항목: `systemctl list-units`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-dependencies%20UNIT%E2%80%A6>.

- `default.target`의 의존성 트리 출력:

`systemctl list-dependencies`

- 특정 유닛의 의존성 트리 출력:

`systemctl list-dependencies {{유닛}}`

- 모든 의존성 유형 포함 (`Requires=`, `Wants=` 뿐만 아니라 전체):

`systemctl list-dependencies {{유닛}} {{[-a|--all]}}`

- 특정 유닛 타입으로 트리 제한:

`systemctl list-dependencies {{유닛}} {{[-t|--type]}} {{service|socket|target|mount|...}}`

- 방향을 반대로 하여 해당 유닛을 의존하는 유닛들 출력:

`systemctl list-dependencies {{유닛}} --reverse`

- 헤더와 푸터 없이 출력 (스크립트용):

`systemctl list-dependencies {{유닛}} --no-legend`
