# gh alias

> GitHub CLI 명령 별칭 관리.
> 더 많은 정보: <https://cli.github.com/manual/gh_alias>.

- `gh`에 설정된 모든 별칭 나열:

`gh alias list`

- `gh` 하위 명령 별칭 생성:

`gh alias set {{pv}} '{{pr view}}'`

- 셸 명령을 `gh` 하위 명령으로 설정:

`gh alias set --shell {{별칭_이름}} {{명령}}`

- 명령 단축키 삭제:

`gh alias delete {{별칭_이름}}`

- 하위 명령 도움말 표시:

`gh alias`
