# jrnl

> 간단한 커맨드라인 저널 애플리케이션.
> 더 많은 정보: <https://jrnl.sh/en/stable/reference-command-line/>.

- 편집기를 사용하여 새 항목 삽입:

`jrnl`

- 빠르게 새 항목 삽입:

`jrnl {{오늘 오전 3시}}: {{제목}}. {{내용}}`

- 최근 열 개의 항목 보기:

`jrnl -n {{10}}`

- 작년 초부터 올해 3월 초까지 발생한 모든 일 보기:

`jrnl -from "{{작년}}" -until {{3월}}`

- "texas" 및 "history" 태그가 있는 모든 항목 편집:

`jrnl {{@texas}} -and {{@history}} --edit`
