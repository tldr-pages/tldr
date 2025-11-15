# choco outdated

> Chocolatey를 사용하여 업데이트가 필요한 패키지 확인.
> 더 많은 정보: <https://chocolatey.org/docs/commands-outdated>.

- 표 형식으로 업데이트가 필요한 패키지 목록 표시:

`choco outdated`

- 고정된 패키지를 출력에서 무시:

`choco outdated --ignore-pinned`

- 패키지를 확인할 사용자 지정 소스 지정:

`choco outdated --source {{source_url|alias}}`

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco outdated --user {{사용자_명}} --password {{비밀번호}}`
