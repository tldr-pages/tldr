# docker compose logs

> Docker Compose 애플리케이션의 컨테이너 출력 로그를 확인.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/compose/logs/>.

- 모든 서비스의 로그 출력:

`docker compose logs`

- 특정 서비스의 로그 출력:

`docker compose logs {{서비스_이름}}`

- 로그를 출력하면서 새로운 로그를 계속 추적 (`tail --follow`와 유사):

`docker compose logs {{[-f|--follow]}}`

- 타임스탬프와 함께 로그 출력:

`docker compose logs {{[-t|--timestamps]}}`

- 각 컨테이너 별로 마지막 `n`줄만 출력:

`docker compose logs {{[-n|--tail]}} {{n}}`

- 특정 시점 이후의 로그만 출력:

`docker compose logs --since {{타임스탬프}}`

- 특정 시점까지의 로그 출력:

`docker compose logs --until {{타임스탬프}}`

- 여러 특정 서비스의 로그 출력:

`docker compose logs {{서비스1 서비스2 ...}}`
