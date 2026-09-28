# poetry sync

> 프로젝트 환경을 `poetry.lock` 파일과 일치하도록 동기화.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#sync>.

- 프로젝트 환경을 `poetry.lock` 파일과 동기화:

`poetry sync`

- 설치에서 하나 이상의 의존성 그룹 제외:

`poetry sync --without {{test|docs|...}}`

- 선택적 의존성 그룹을 포함하여 설치:

`poetry sync --with {{test|docs|...}}`

- 선택적 그룹을 포함한 모든 의존성 그룹 설치:

`poetry sync --all-groups`

- 지정한 의존성 그룹만 설치:

`poetry sync --only {{test|docs|...}}`

- 의존성 없이 프로젝트 자체만 설치:

`poetry sync --only-root`

- 설치할 extra 지정:

`poetry sync {{[-E|--extras]}}`

- 프로젝트 자체 설치 없이 의존성만 동기화:

`poetry sync --no-root`
