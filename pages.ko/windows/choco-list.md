# choco list

> Chocolatey로 패키지 목록 표시.
> 더 많은 정보: <https://chocolatey.org/docs/commands-list>.

- 사용 가능한 모든 패키지 표시:

`choco list`

- 로컬에 설치된 모든 패키지 표시:

`choco list --local-only`

- 로컬 프로그램을 포함한 목록 표시:

`choco list --include-programs`

- 승인된 패키지만 표시:

`choco list --approved-only`

- 사용자 정의 소스를 지정하여 패키지 표시:

`choco list --source {{소스_url|별칭}}`

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco list --user {{사용자_명}} --password {{비밀번호}}`
