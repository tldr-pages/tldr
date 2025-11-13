# awslogs

> Amazon CloudWatch 로그에서 그룹, 스트림 및 이벤트를 쿼리.
> 더 많은 정보: <https://github.com/jorgebastida/awslogs>.

- 로그 그룹 나열:

`awslogs groups`

- 지정된 그룹의 기존 스트림을 나열:

`awslogs streams {{/var/log/syslog}}`

- 1~2시간 전 사이에 지정된 그룹의 모든 스트림에 대한 로그를 가져옴:

`awslogs get {{/var/log/syslog}} {{[-s|--start]}} '{{2h ago}}' {{[-e|--end]}} '{{1h ago}}'`

- 특정 CloudWatch Logs 필터 패턴과 일치하는 로그 가져오기:

`awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern '{{ERROR}}'`

- 지정된 그룹의 모든 스트림에 대한 로그를 감시:

`awslogs get {{/var/log/syslog}} ALL --watch`
