# rabbitmqctl-users

> RabbitMQ 사용자와 해당 사용자의 권한 및 태그를 관리.
> 더 많은 정보: <https://www.rabbitmq.com/docs/management>.

- 모든 사용자 목록 표시:

`rabbitmqctl list_users`

- 비밀번호를 지정하여 새로운 사용자 추가:

`rabbitmqctl add_user {{사용자명}} {{비밀번호}}`

- 기존 사용자 삭제:

`rabbitmqctl delete_user {{사용자명}}`

- 사용자 비밀번호 변경:

`rabbitmqctl change_password {{사용자명}} {{새로운_비밀번호}}`

- 지정한 가상 호스트에서 사용자의 권한 설정:

`rabbitmqctl set_permissions {{[-p|--vhost]}} {{vhost}} {{사용자명}} {{read}} {{write}} {{configure}}`

- 지정한 가상 호스트에서 사용자의 모든 권한 제거:

`rabbitmqctl clear_permissions {{[-p|--vhost]}} {{vhost}} {{사용자명}}`

- 사용자에게 하나 이상의 태그(예: `administrator`) 할당:

`rabbitmqctl set_user_tags {{사용자명}} {{태그1 태그2 ...}}`
