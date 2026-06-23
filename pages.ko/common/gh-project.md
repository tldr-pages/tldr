# gh project

> GitHub Projects 작업 수행.
> 더 많은 정보: <https://cli.github.com/manual/gh_project>.

- 현재 인증된 사용자가 소유한 프로젝트 목록 표시:

`gh project {{[ls|list]}}`

- 특정 사용자 또는 조직이 소유한 프로젝트 목록 표시:

`gh project {{[ls|list]}} --owner {{소유자}}`

- 숫자로 프로젝트 조회:

`gh project view {{숫자}} --owner {{소유자}}`

- 새로운 프로젝트 생성:

`gh project create --owner {{소유자}} --title {{프로젝트_제목}}`

- 프로젝트에 항목(issue 또는 pull request) 추가:

`gh project item-add {{숫자}} --owner {{소유자}} --url {{이슈_또는_PR_주소}}`

- 프로젝트의 항목 목록 표시:

`gh project item-list {{숫자}} --owner {{소유자}}`

- 프로젝트 종료:

`gh project close {{숫자}} --owner {{소유자}}`
