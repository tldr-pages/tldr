# poetry build

> Poetry 패키지를 tarball과 wheel 형식으로 빌드.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#build>.

- 프로젝트의 tarball과 wheel 패키지 빌드:

`poetry build`

- wheel 패키지 빌드:

`poetry build {{[-f|--format]}} wheel`

- 소스 배포판(sdist) 빌드:

`poetry build {{[-f|--format]}} sdist`

- 빌드 전에 출력 디렉터리 정리:

`poetry build --clean`

- 출력 디렉터리 지정:

`poetry build {{[-o|--output]}} {{경로/대상/디렉터리}}`
