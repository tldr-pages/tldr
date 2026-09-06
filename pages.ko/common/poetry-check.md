# poetry check

> Poetry 설정 파일의 유효성과 일관성을 검사.
> 관련 항목: `asdf`.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#check>.

- `pyproject.toml`과 `poetry.lock`의 유효성 및 일관성 검사:

`poetry check`

- `poetry.lock` 파일이 존재하는지 확인:

`poetry check --lock`

- 경고가 발생하면 검사 실패로 처리:

`poetry check --strict`
