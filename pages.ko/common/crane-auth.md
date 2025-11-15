# crane auth

> 로그인하거나 자격 증명에 액세스.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_auth.md>.

- `crane auth` 하위명령어를 실행:

`crane auth {{하위명령어}}`

- 자격증명 도우미 구현:

`crane auth get {{레지스트리_주소}} {{[-h|--help]}}`

- 레지스트리에 로그인:

`crane auth login {{레지스트리_주소}} {{[-h|--help]}} {{[-p|--password]}} {{비밀번호}} {{-password-stdin}} {{[-u|--username]}} {{사용자명}}`

- 레지스트리에서 로그아웃:

`crane auth logout {{레지스트리_주소}} {{[-h|--help]}}`

- 원격 저장소에 대한 토큰을 검색:

`crane auth token {{레지스트리_주소}} {{[-H|--header]}} {{[-h|--help]}} {{[-m|--mount]}} {{스코프1 스코프2 ...}} --push`

- 도움말 표시:

`crane auth {{[-h|--help]}}`
