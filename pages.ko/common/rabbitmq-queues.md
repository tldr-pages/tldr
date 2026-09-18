# rabbitmq-queues

> RabbitMQ 큐를 관리.
> 더 많은 정보: <https://www.rabbitmq.com/docs/man/rabbitmq-queues.8>.

- 지정한 노드에 멤버를 추가하여 quorum queue 클러스터 확장:

`rabbitmq-queues grow {{노드}} {{all|even}}`

- 복제된 큐의 리더를 노드 간에 재분해:

`rabbitmq-queues rebalance {{all|quorum|stream}}`

- 지정한 노드의 멤버를 제거하여 quorum queue 클러스터 축소:

`rabbitmq-queues shrink {{노드}}`

- 지정한 노드의 quorum queue 멤버 추가:

`rabbitmq-queues add_member {{큐}} {{노드}}`

- 지정한 노드의 quorum queue 멤버 삭제:

`rabbitmq-queues delete_member {{큐}} {{노드}}`

- quorum queue의 quorum 상태 표시:

`rabbitmq-queues quorum_status {{큐}}`
