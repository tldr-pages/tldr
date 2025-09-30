# icalBuddy

> macOS 캘린더 데이터베이스에서 이벤트와 작업을 출력하는 명령줄 유틸리티.
> 더 많은 정보: <https://hasseg.org/icalBuddy/>.

- 오늘 나중에 있을 이벤트 표시:

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- 완료되지 않은 작업 표시:

`icalBuddy uncompletedTasks`

- 오늘 모든 이벤트를 캘린더별로 구분하여 서식화된 목록으로 표시:

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- 지정된 일수 동안의 작업 표시:

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+{{일_수}}"`

- 특정 기간 내의 이벤트 표시:

`icalBuddy eventsFrom:{{시작_날짜}} to:{{종료_날짜}}`
