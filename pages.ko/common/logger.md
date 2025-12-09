# logger

> 메시지를 syslog (/var/log/syslog)에 추가.
> 더 많은 정보: <https://manned.org/logger.1p>.

- 메시지를 syslog에 기록:

`logger {{메시지}}`

- `stdin`에서 입력을 받아 syslog에 기록:

`echo {{로그_항목}} | logger`

- 지정된 포트에서 실행 중인 원격 syslog 서버로 출력 전송. 기본 포트는 514:

`echo {{로그_항목}} | logger --server {{호스트명}} --port {{포트}}`

- 기록된 모든 줄에 특정 태그 사용. 기본값은 로그인한 사용자 이름:

`echo {{로그_항목}} | logger --tag {{태그}}`

- 주어진 우선순위로 메시지 기록. 기본값은 `user.notice`. 모든 우선순위 옵션은 `man logger` 참조:

`echo {{로그_항목}} | logger --priority {{user.warning}}`
