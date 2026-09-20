# poetry add

> Poetry 프로젝트의 `pyproject.toml` 파일에 필요한 패키지를 추가.
> 관련 항목: `asdf`.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#add>.

- 필요한 패키지 추가:

`poetry add {{패키지_이름}}`

- 지정한 의존성 그룹에 필요한 패키지 추가:

`poetry add {{패키지_이름}} --group {{그룹_이름}}`

- 지정한 버전의 패키지 추가:

`poetry add {{패키지_이름}}=={{버전}}`

- 지정한 버전 이하의 패키지 추가:

`poetry add {{패키지_이름}}<={{버전}}`

- 지정한 버전 이상의 패키지 추가:

`poetry add {{패키지_이름}}>={{버전}}`
