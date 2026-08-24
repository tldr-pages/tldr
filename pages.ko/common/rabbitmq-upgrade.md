# rabbitmq-upgrade

> RabbitMQ 노드의 업그레이드를 관리.
> 더 많은 정보: <https://www.rabbitmq.com/docs/man/rabbitmq-upgrade.8>.

- 모든 quorum queue가 최소 요구치를 초과하는 온라인 quorum 상태가 될 때까지 대기:

`rabbitmq-upgrade await_online_quorum_plus_one`

- 노드를 유지보수 모드로 전환:

`rabbitmq-upgrade drain`

- 노드를 유지보수 모드에서 해제하고 일반 운영 모드로 전환:

`rabbitmq-upgrade revive`

- 업그레이드 후 작업 실행:

`rabbitmq-upgrade post_upgrade`

- 도움말 표시:

`rabbitmq-upgrade help`
