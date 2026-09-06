# uv version

> 프로젝트 버전 조회 또는 업데이트.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-version>.

- 현재 프로젝트 버전 표시:

`uv version`

- 프로젝트 버전을 지정한 값으로 설정:

`uv version {{1.2.3}}`

- semantic versioning에 따라 프로젝트 버전 증가:

`uv version --bump {{major|minor|patch}}`

- `pyproject.toml`을 변경하지 않고 버전 변경 사항 미리보기:

`uv version --bump {{패치}} --dry-run`

- workspace의 지정한 패키지 버전 업데이트:

`uv version --package {{패키지_이름}} {{1.2.3}}`

- 버전 정보를 JSON 형식으로 표시:

`uv version --output-format json`
