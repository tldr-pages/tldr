# choco search

> Chocolatey로 로컬 또는 원격 패키지를 검색.
> 더 많은 정보: <https://chocolatey.org/docs/commands-search>.

- 패키지 검색:

`choco search {{쿼리}}`

- 로컬에서 패키지 검색:

`choco search {{쿼리}} --local-only`

- 결과에서 정확히 일치하는 항목만 포함:

`choco search {{쿼리}} --exact`

- 모든 프롬프트를 자동으로 확인:

`choco search {{쿼리}} --yes`

- 패키지 검색을 위한 사용자 지정 소스 지정:

`choco search {{쿼리}} --source {{소스_url|별칭}}`

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco search {{쿼리}} --user {{사용자_명}} --password {{비밀번호}}`
