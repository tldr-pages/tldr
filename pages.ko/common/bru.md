# bru

> API 탐색 및 테스트를 위한 오픈소스 IDE인 Bruno용 CLI.
> 더 많은 정보: <https://docs.usebruno.com/bru-cli/overview>.

- 현재 디렉터리에서 모든 요청된 파일을 실행:

`bru run`

- 파일 이름을 지정하여, 현재 디렉터리에서 단일 요청을 실행:

`bru run {{file.bru}}`

- 환경 파일을 사용해 요청을 실행:

`bru run --env {{환경_이름}}`

- 변수가 있는 환경을 사용하여 요청을 실행:

`bru run --env {{환경_이름}} --env-var {{변수_이름}}={{변수_값}}`

- 요청을 실행하고, 출력 파일에 결과를 수집:

`bru run --output {{경로/대상/출력.json}}`

- 도움말 표시:

`bru run --help`
