# poetry-self

> Poetry 자체 설치/런타임 환경을 관리.
> Poetry 설정 디렉터리의 `pyproject.toml`과 `poetry.lock` 파일을 사용.
> 관련 항목: `asdf`.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#self>.

- 패키지 설치:

`poetry self add {{패키지_이름}}`

- Poetry 설치 환경의 `pyproject.toml` 파일에 정의된 의존성 설치:

`poetry self install`

- Poetry 설치 환경의 `pyproject.toml` 파일에 정의된 의존성 잠금:

`poetry self lock`

- 패키지 제거:

`poetry self remove {{패키지_이름}}`

- 설치된 모든 패키지 목록 표시:

`poetry self show`

- 설치된 모든 플러그인 목록 표시:

`poetry self show plugins`

- Poetry 런타임 환경을 설치 환경의 `poetry.lock` 파일과 동기화:

`poetry self sync`

- Poetry 설치 환경의 `pyproject.toml` 파일을 기준으로 의존성 업데이트:

`poetry self update`
