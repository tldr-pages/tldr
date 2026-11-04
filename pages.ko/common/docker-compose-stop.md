# docker compose stop

> 실행 중인 컨테이너를 삭제하지 않고 중지.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/compose/stop>.

- 실행 중인 모든 서비스 중지:

`docker compose stop`

- 지정한 서비스 중지:

`docker compose stop {{서비스_1 서비스_2 ...}}`

- 종료 대기 시간을 지정하여 서비스 중지:

`docker compose stop {{[-t|--timeout]}} {{초}}`

- 지정한 compose 파일에 정의된 서비스 중지:

`docker compose {{[-f|--file]}} {{경로/대상/compose_파일}} stop`

- Dry run 수행 (실제 실행하지 않고 수행 예정 작업만 표시):

`docker compose stop --dry-run`

- 종료 대기 시간을 지정하여 특정 서비스 중지:

`docker compose stop {{[-t|--timeout]}} {{초}} {{서비스_1 서비스_2 ...}}`
