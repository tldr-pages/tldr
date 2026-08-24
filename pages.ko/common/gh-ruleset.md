# gh ruleset

> GitHub 저장소 규칙모음 관리.
> 더 많은 정보: <https://cli.github.com/manual/gh_ruleset>.

- 현재 저장소의 모든 규칙모음 목록 표시:

`gh {{[rs|ruleset]}} {{[ls|list]}}`

- 특정 조직의 모든 규칙모음 목록 표시:

`gh {{[rs|ruleset]}} {{[ls|list]}} {{[-o|--org]}} {{조직_이름}}`

- 현재 브랜치에 적용되는 규칙 확인:

`gh {{[rs|ruleset]}} check`

- 다른 저장소의 특정 브랜치에 적용되는 규칙 확인:

`gh {{[rs|ruleset]}} check {{브랜치_이름}} {{[-R|--repo]}} {{소유자}}/{{저장소}}`

- 현재 저장소의 규칙모음을 대화형으로 선택하여 보기:

`gh {{[rs|ruleset]}} view`

- ID로 특정 규칙모음 보기:

`gh {{[rs|ruleset]}} view {{규칙모음_아이디}}`

- ID로 조직 수준 규칙모음 보기:

`gh {{[rs|ruleset]}} view {{규칙모음_아이디}} {{[-o|--org]}} {{조직_이름}}`

- 특정 저장소의 규칙모음 목록을 브라우저에서 열기:

`gh {{[rs|ruleset]}} {{[ls|list]}} {{[-R|--repo]}} {{소유자}}/{{저장소}} {{[-w|--web]}}`
