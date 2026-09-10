# poetry source

> Poetry 프로젝트의 패키지 소스 설정을 관리.
> 관련 항목: `asdf`.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#source>.

- 소스 설정 추가:

`poetry source add {{소스_이름}} {{소스_주소}}`

- 소스의 우선순위 설정:

`poetry source add --priority {{primary|supplemental|explicit}} {{소스_이름}} {{소스_주소}}`

- 모든 소스 정보 표시:

`poetry source show`

- 지정한 소스 정보 표시:

`poetry source show {{소스_이름}}`

- `pyproject.toml` 파일에서 지정한 소스 제거:

`poetry source remove {{소스_이름}}`
