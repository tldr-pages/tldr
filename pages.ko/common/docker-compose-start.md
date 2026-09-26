# docker compose start

> 서비스의 기존 컨테이너를 시작.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/compose/start/>.

- 모든 서비스의 기존 컨테이너 시작:

`docker compose start`

- 하나 이상의 지정한 서비스의 기존 컨테이너 시작:

`docker compose start {{서비스1 서비스2 ...}}`

- 기존 컨테이너를 실제로 시작하지 않고 실행 과정 미리 확인:

`docker compose start --dry-run`

- 기존 컨테이너를 시작하고 서비스가 실행 중이거나 정상 상태가 될 때까지 대기:

`docker compose start --wait`

- 기존 컨테이너를 시작하고 지정한 시간(초) 동안 서비스가 준비될 때까지 대기:

`docker compose start --wait --wait-timeout {{초}}`
