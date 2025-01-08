# sui move

> Move 소스 코드를 다루기 위한 도구.
> 더 많은 정보: <https://docs.sui.io/references/cli/move>.

- 지정된 폴더에 새 Move 프로젝트 생성:

`sui move new {{프로젝트_이름}}`

- 현재 디렉토리에서 Move 프로젝트 테스트:

`sui move test`

- 커버리지와 함께 테스트하고 요약 얻기:

`sui move test --coverage; sui move coverage summary`

- 테스트에서 코드의 어느 부분이 커버되었는지 찾기 (즉, 커버리지 결과 설명):

`sui move coverage source --module {{모듈_이름}}`

- 현재 디렉토리에서 Move 프로젝트 빌드:

`sui move build`

- 지정된 경로에서 Move 프로젝트 빌드:

`sui move build --path {{경로}}`

- 제공된 경로에 있는 패키지를 Move 2024로 마이그레이션:

`sui move migrate {{경로}}`
