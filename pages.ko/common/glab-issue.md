# glab issue

> GitLab 이슈 관리.
> 더 많은 정보: <https://glab.readthedocs.io/en/latest/issue>.

- 특정 이슈 표시:

`glab issue view {{이슈_번호}}`

- 기본 웹 브라우저에 특정 문제를 표시:

`glab issue view {{이슈_번호}} --web`

- 기본 웹 브라우저에 새로운 이슈를 생성:

`glab issue create --web`

- `bug` 라벨이 있는 최근 10개 문제를 나열:

`glab issue list --per-page {{10}} --label "{{bug}}"`

- 특정 사용자가 작성한 닫힌 이슈를 나열:

`glab issue list --closed --author {{사용자명}}`

- 특정 이슈 다시 열기:

`glab issue reopen {{이슈_번호}}`
