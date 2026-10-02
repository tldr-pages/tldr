# poetry version

> Poetry 프로젝트 버전 관리.
> `patch`, `minor`, `major`, `prepatch`, `preminor`, `premajor`, `prerelease` 등의 버전 단계를 지원.
> 관련 항목: `asdf`.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#version>.

- 현재 버전만 출력:

`poetry version {{[-s|--short]}}`

- 프로젝트 버전을 지정한 단계로 변경:

`poetry version {{단계}}`

- 프로젝트 버전을 다음 사전 릴리스 단계로 변경:

`poetry version --next-phase`

- `pyproject.toml`을 수정하지 않고 버전 단계 변경 결과 확인:

`poetry version {{단계}} --dry-run`
