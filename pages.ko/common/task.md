# task

> 명령줄 할 일 목록 관리 도구.
> 더 많은 정보: <https://taskwarrior.org/docs/>.

- 내일까지 완료해야 할 새로운 작업 추가:

`task add {{설명}} due:{{내일}}`

- 작업의 우선순위 업데이트:

`task {{작업_ID}} modify priority:{{H|M|L}}`

- 작업 완료:

`task {{작업_ID}} done`

- 작업 삭제:

`task {{작업_ID}} delete`

- 모든 열려 있는 작업 나열:

`task list`

- 이번 주 말까지 마감인 열려 있는 작업 나열:

`task list due.before:{{주말}}`

- 일별 그래픽 번다운 차트 표시:

`task burndown.daily`

- 모든 보고서 나열:

`task reports`
