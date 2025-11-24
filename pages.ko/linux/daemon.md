# daemon

> 프로세스를 데몬으로 실행.
> 더 많은 정보: <https://manned.org/daemon.1>.

- 명령어를 데몬으로 실행:

`daemon --name="{{이름}}" {{명령어}}`

- 명령어를 데몬으로 실행하고, 충돌 시 재시작:

`daemon --name="{{이름}}" --respawn {{명령어}}`

- 충돌 시 재시작하는 데몬으로 명령어를 실행하며, 10초마다 두 번 시도:

`daemon --name="{{이름}}" --respawn --attempts=2 --delay=10 {{명령어}}`

- 로그를 특정 파일에 기록하며 명령어를 데몬으로 실행:

`daemon --name="{{이름}}" --errlog={{경로/대상/파일.log}} {{명령어}}`

- 데몬 종료 (SIGTERM):

`daemon --name="{{이름}}" --stop`

- 데몬 목록 나열:

`daemon --list`
