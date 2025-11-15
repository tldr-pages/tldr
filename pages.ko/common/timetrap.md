# timetrap

> Ruby로 작성된 간단한 명령줄 시간 추적기.
> 더 많은 정보: <https://github.com/samg/timetrap>.

- 새 타임시트 생성:

`timetrap sheet {{타임시트}}`

- 5분 전에 시작된 항목 체크인:

`timetrap in --at "{{5분 전}}" {{항목_노트}}`

- 현재 타임시트 표시:

`timetrap display`

- 마지막 항목의 종료 시간 수정:

`timetrap edit --end {{시간}}`
