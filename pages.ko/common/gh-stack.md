# gh stack

> 스택 형태로 연결된 브랜치와 Pull Request를 관리하는 GitHub CLI 확장 기능.
> 더 많은 정보: <https://docs.github.com/en/pull-requests/reference/stacked-prs-cli-commands>.

- 대화형으로 새로운 스택 시작(첫 번째 브랜치를 생성하고 체크아웃):

`gh stack init`

- 브랜치 이름을 미리 지정하여 새 스택 시작:

`gh stack init {{브랜치_이름1 브랜치_이름2 ...}}`

- 스택 최상단에 브랜치 추가:

`gh stack add {{브랜치_이름}}`

- 모든 브랜치를 기본 원격 저장소에 푸시:

`gh stack push`

- 모든 브랜치를 지정한 원격 저장소에 푸시:

`gh stack push --remote {{원격_저장소_이름}}`

- 스택 구조 표시:

`gh stack view`

- 스택에 포함된 PR 생성:

`gh stack submit`
