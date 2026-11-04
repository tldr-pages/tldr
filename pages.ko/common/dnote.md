# dnote

> 명령어, 코드 조각 및 노트를 기록하고 여러 장치에서 사용할 수 있는 노트북 도구.
> 더 많은 정보: <https://www.getdnote.com/docs/cli/commands/>.

- 설정된 편집기에서 지정한 책에 노트 추가:

`dnote add {{책_이름}}`

- 인라인 내용을 지정하여 노트 추가:

`dnote add {{책_이름}} {{[-c|--content]}} "{{노트_내용}}"`

- 모든 책과 노트 목록 표시:

`dnote view`

- 지정한 책의 모든 노트 표시:

`dnote view {{책_이름}}`

- 전체 텍스트 검색을 사용하여 노트 검색:

`dnote find "{{키워드}}"`

- ID를 지정해 노트 편집:

`dnote edit {{노트_아이디}}`

- 노트 또는 전체 책 삭제:

`dnote remove {{노트_아이디|책_이름}}`

- Dnote 서버와 노트 동기화:

`dnote sync`
