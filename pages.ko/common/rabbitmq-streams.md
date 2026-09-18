# rabbitmq-streams

> RabbitMQ 스트림 관리.
> 더 많은 정보: <https://www.rabbitmq.com/docs/man/rabbitmq-streams.8>.

- 지정한 노드에 스트림 복제본 추가:

`rabbitmq-streams add_replica {{스트림}} {{노드}}`

- 지정한 노드의 스트림 복제본 삭제:

`rabbitmq-streams delete_replica {{스트림}} {{노드}}`

- 스트림 상태 표시:

`rabbitmq-streams stream_status {{스트림}}`

- 스트림 재시작:

`rabbitmq-streams restart_stream {{스트림}}`

- 스트림 연결 목록 표시:

`rabbitmq-streams list_stream_connections`

- 모든 스트림 소비자 목록 표시:

`rabbitmq-streams list_stream_consumers`

- 모든 스트림 발행자 목록 표시:

`rabbitmq-streams list_stream_publishers`

- 스트림의 추적 정보 표시:

`rabbitmq-streams list_stream_tracking {{스트림}}`
