# khal

> 명령줄에서 사용하는 텍스트 기반 캘린더 및 일정 관리 애플리케이션.
> 더 많은 정보: <https://lostpackets.de/khal>.

- 상호작용 모드에서 Khal 시작:

`ikhal`

- 개인 캘린더에 예정된 다음 7일 동안의 모든 이벤트 출력:

`khal list -a {{personal}} {{today}} {{7d}}`

- 개인 캘린더가 아닌 내일 10:00에 예정된 모든 이벤트 출력:

`khal at -d {{personal}} {{tomorrow}} {{10:00}}`

- 다음 3개월 동안의 이벤트 목록이 포함된 캘린더 출력:

`khal calendar`

- 개인 캘린더에 새 이벤트 추가:

`khal new -a {{personal}} {{2020-09-08}} {{18:00}} {{18:30}} "{{치과 예약}}"`
