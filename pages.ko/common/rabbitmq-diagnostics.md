# rabbitmq-diagnostics

> RabbitMQ 노드의 진단, 모니터링 및 상태 점검을 수행.
> 많은 하위 명령어는 `rabbitmqctl`에 위임됨.
> 더 많은 정보: <https://www.rabbitmq.com/docs/man/rabbitmq-diagnostics.8>.

- 리소스 경보 목록 표시:

`rabbitmq-diagnostics alarms`

- 노드의 인증서 목록 표시:

`rabbitmq-diagnostics certificates`

- 지정한 노드에서 RabbitMQ가 실행 중인지 확인:

`rabbitmq-diagnostics check_running --node {{노드}}`

- 피어 탐색 수행:

`rabbitmq-diagnostics discover_peers`

- 리스너 목록 표시 (바인딩된 소켓):

`rabbitmq-diagnostics listeners`

- 지정한 노드의 최근 로그 `n`줄 출력:

`rabbitmq-diagnostics log_tail --number {{숫자}} --node {{노드}}`
