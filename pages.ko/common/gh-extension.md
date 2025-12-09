# gh extension

> GitHub CLI 확장 관리.
> 더 많은 정보: <https://cli.github.com/manual/gh_extension>.

- 동일한 이름의 디렉토리에 새로운 GitHub CLI 확장 프로젝트 초기화:

`gh extension create {{확장_이름}}`

- GitHub 저장소에서 확장 설치:

`gh extension install {{소유자}}/{{저장소}}`

- 설치된 확장 나열:

`gh extension list`

- 특정 확장 업그레이드:

`gh extension upgrade {{확장_이름}}`

- 모든 확장 업그레이드:

`gh extension upgrade --all`

- 설치된 확장 나열:

`gh extension list`

- 확장 제거:

`gh extension remove {{확장_이름}}`

- 하위 명령에 대한 도움말 표시:

`gh extension {{하위_명령}} --help`
