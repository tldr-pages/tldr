# poetry config

> poetry 설정과 저장소를 관리.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#config>.

- 현재 설정 목록 표시:

`poetry config --list`

- 이전에 설정한 항목 제거:

`poetry config {{설정_키}} --unset`

- 지정한 설정값 표시:

`poetry config {{설정_키}}`

- 설정 이름 뒤에 값을 지정해 기존 설정을 변경하거나 새로운 설정 추가:

`poetry config {{설정_키}} {{설정_값}}`

- 오래된 설정을 현재 형식으로 마이그레이션:

`poetry config --migrate`

- 현재 프로젝트에만 적용되는 설정 지정/조회:

`poetry config --local`
