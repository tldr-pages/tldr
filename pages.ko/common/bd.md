# bd

> AI 코딩 에이전트를 위한 경량 메모리 시스템 및 Git 기반 이슈 트래커.
> 더 많은 정보: <https://github.com/steveyegge/beads#usage>.

- 프로젝트 데이터베이스 초기화:

`bd init`

- 설명, 우선순위, 유형을 포함해 새로운 이슈를 생성:

`bd create {{이슈_제목}} {{[-d|--description]}} {{설명}} {{[-p|--priority]}} {{1}} {{[-t|--type]}} {{bug|feature|task|epic|chore}}`

- 모든 이슈 나열:

`bd list`

- 작업을 바로 시작할 수 있는 이슈 (차단 요소 없음)을 표시:

`bd ready`

- 특정 이슈의 상세내용 표시:

`bd show {{이슈_번호}}`

- 이슈 상태 업데이트:

`bd update {{이슈_아이디}} {{[-s|--status]}} {{open|in_progress|blocked|closed}}`

- 변경 사항을 수동으로 동기화하고, Git에서 최신 내용을 가져오기:

`bd sync`

- 도움말 표시:

`bd {{[-h|--help]}}`
