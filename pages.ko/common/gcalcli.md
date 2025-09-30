# gcalcli

> Google 캘린더와 상호작용.
> 처음 실행 시 Google API 인증을 요청.
> 더 많은 정보: <https://github.com/insanum/gcalcli>.

- 향후 7일 동안의 모든 캘린더에 대한 이벤트를 나열:

`gcalcli agenda`

- 특정 날짜부터 또는 그 사이에 시작되는 이벤트 표시(예: "내일"과 같은 상대 날짜도 사용):

`gcalcli agenda {{mm/dd}} [{{mm/dd}}]`

- 특정 캘린더의 이벤트 나열:

`gcalcli --calendar {{캘린더_이름}} agenda`

- 주별 이벤트의 ASCII 달력을 표시:

`gcalcli calw`

- 한 달 동안의 이벤트에 대한 ASCII 달력을 표시:

`gcalcli calm`

- 캘린더에 이벤트를 빠르게 추가:

`gcalcli --calendar {{캘린더_이름}} quick "{{mm/dd}} {{HH:MM}} {{이벤트_이름}}"`

- 캘린더에 이벤트를 추가. 대화형 프롬프트를 트리거:

`gcalcli --calendar "{{캘린더_이름}}" add`
