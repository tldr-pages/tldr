# gh config

> GitHub CLI의 설정 변경.
> 더 많은 정보: <https://cli.github.com/manual/gh_config>.

- 사용 중인 Git 프로토콜 표시:

`gh config get git_protocol`

- 프로토콜을 SSH로 설정:

`gh config set git_protocol {{ssh}}`

- 모든 `gh` 명령어의 기본 페이지로 `delta`를 나란히 보기 모드로 사용:

`gh config set pager '{{delta --side-by-side}}'`

- 텍스트 편집기를 Vim으로 설정:

`gh config set editor {{vim}}`

- 기본 텍스트 편집기로 재설정:

`gh config set editor ""`

- 대화형 프롬프트 비활성화:

`gh config set prompt {{disabled}}`

- 특정 설정 값 설정:

`gh config set {{key}} {{value}}`
