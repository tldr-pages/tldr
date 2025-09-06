# choco info

> Chocolatey를 사용하여 패키지에 대한 자세한 정보 표시.
> 더 많은 정보: <https://chocolatey.org/docs/commands-info>.

- 특정 패키지에 대한 정보 표시:

`choco info {{패키지}}`

- 로컬 패키지에 대한 정보만 표시:

`choco info {{패키지}} --local-only`

- 패키지 정보를 받을 사용자 지정 소스 지정:

`choco info {{패키지}} --source {{source_url|별칭}}`

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco info {{사용자_명}} --user {{사용자_명}} --password {{비밀번호}}`
