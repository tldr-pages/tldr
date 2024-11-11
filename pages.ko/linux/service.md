# service

> init 스크립트를 실행하여 서비스를 관리.
> 전체 스크립트 경로는 생략해야 하며(`/etc/init.d/`가 기본값으로 가정됩니다).
> 더 많은 정보: <https://manned.org/service>.

- 모든 서비스의 이름 및 상태 나열:

`service --status-all`

- 서비스 시작/중지/재시작/다시 로드 (시작/중지는 항상 가능해야 함):

`service {{서비스_이름}} {{start|stop|restart|reload}}`

- 전체 재시작 수행 (시작과 중지로 스크립트를 두 번 실행):

`service {{서비스_이름}} --full-restart`

- 서비스의 현재 상태 표시:

`service {{서비스_이름}} status`
