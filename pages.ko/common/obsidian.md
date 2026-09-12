# obsidian

> Obsidian Markdown 노트 애플리케이션을 위한 명령줄 인터페이스.
> 참고: Obsidian 애플리케이션이 실행되어 있어야 함.
> 더 많은 정보: <https://obsidian.md/help/cli>.

- 오늘의 데일리 노트 열기:

`obsidian daily`

- 오늘의 데일리 노트에 작업 항목 추가:

`obsidian daily:append content="- [ ] {{task}}"`

- 템플릿을 사용하여 새로운 노트 생성:

`obsidian create name="{{노트_이름}}" template={{템플릿_이름}}`

- vault에서 텍스트 검색:

`obsidian search query="{{검색_텍스트}}"`

- vault의 모든 미완료 작업 목록 표시:

`obsidian tasks todo`

- 지정한 노트 열기:

`obsidian read file={{노트_이름}}`

- vault 루트를 기준으로 지정한 경로의 노트 읽기:

`obsidian read path={{경로/대상/노트.md}}`

- 현재 활성화된 노트 읽기:

`obsidian read`