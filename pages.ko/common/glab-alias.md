# glab alias

> GitLab CLI 명령어 별칭을 관리.
> 더 많은 정보: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/alias/index.md>.

- 하위 명령어 도움말을 표시:

`glab alias`

- `glab`이 사용하도록 구성된 모든 별칭을 나열:

`glab alias list`

- `glab` 하위 명령 별칭을 생성:

`glab alias set {{mrv}} '{{mr view}}'`

- 쉘 명령을 `glab` 하위 명령으로 설정:

`glab alias set {{[-s|--shell]}} {{alias_이름}} {{명령어}}`

- 명령 단축키 삭제:

`glab alias delete {{alias_이름}}`
