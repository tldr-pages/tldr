# dockerd

> Docker 컨테이너를 시작하고 관리하는 지속적인 프로세스.
> 더 많은 정보: <https://docs.docker.com/reference/cli/dockerd/>.

- Docker 데몬 실행:

`dockerd`

- Docker 데몬을 실행하고 특정 소켓(UNIX 및 TCP)을 수신하도록 설정:

`dockerd --host unix://{{경로/대상/tmp.sock}} --host tcp://{{IP}}`

- 특정 데몬 PID 파일로 실행:

`dockerd --pidfile {{경로/대상/PID_파일}}`

- 디버그 모드로 실행:

`dockerd --debug`

- 특정 로그 레벨로 실행:

`dockerd --log-level {{debug|info|warn|error|fatal}}`
