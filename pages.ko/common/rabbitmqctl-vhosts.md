# rabbitmqctl-vhosts

> RabbitMQ의 가상 호스트(vhost)를 관리.
> Vhost는 하나의 RabbitMQ 서버에서 여러 논리적 브로커를 분리하는 데 사용.
> 더 많은 정보: <https://www.rabbitmq.com/docs/vhosts>.

- 모든 가상 호스트 목록 표시:

`rabbitmqctl list_vhosts`

- 새 가상 호스트 추가:

`rabbitmqctl add_vhost {{vhost_이름}}`

- 가상 호스트 삭제:

`rabbitmqctl delete_vhost {{vhost_이름}}`

- 지정한 가상 호스트에서 사용자의 권한 설정:

`rabbitmqctl set_permissions {{[-p|--vhost]}} {{vhost_이름}} {{사용자명}} {{read}} {{write}} {{configure}}`

- 지정한 가상 호스트에서 사용자의 권한 제거:

`rabbitmqctl clear_permissions {{[-p|--vhost]}} {{vhost_이름}} {{사용자명}}`
