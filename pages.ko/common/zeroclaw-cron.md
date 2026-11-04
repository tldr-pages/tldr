# zeroclaw cron

> ZeroClaw의 예약 작업을 관리.
> 더 많은 정보: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- 예약된 모든 작업 목록 표시:

`zeroclaw cron list`

- cron 표현식을 사용하여 새로운 예약 작업 추가:

`zeroclaw cron add "{{* * * * *}}" "{{명령어}}"`

- 한 번만 실행되는 지연 작업 추가:

`zeroclaw cron once {{30m|1h|1d|...}} "{{명령어}}"`

- 예약 작업 제거:

`zeroclaw cron remove {{작업_아이디}}`

- 예약 작업 일시 중지:

`zeroclaw cron pause {{작업_아이디}}`

- 일시 중지된 작업 다시 시작:

`zeroclaw cron resume {{작업_아이디}}`

- 도움말 표시:

`zeroclaw cron {{[-h|--help]}}`
