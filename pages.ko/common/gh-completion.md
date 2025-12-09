# gh completion

> GitHub CLI 명령어에 대한 셸 자동완성 스크립트 생성.
> 더 많은 정보: <https://cli.github.com/manual/gh_completion>.

- 자동완성 스크립트 출력:

`gh completion --shell {{bash|zsh|fish|powershell}}`

- `gh` 자동완성 스크립트를 `~/.bashrc`에 추가:

`gh completion --shell {{bash}} >> {{~/.bashrc}}`

- `gh` 자동완성 스크립트를 `~/.zshrc`에 추가:

`gh completion --shell {{zsh}} >> {{~/.zshrc}}`

- 하위 명령어 도움말 표시:

`gh completion`
