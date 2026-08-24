# docker compose up

> Compose 파일에 정의된 Docker 서비스를 시작하고 실행.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/compose/up/>.

- docker-compose 파일에 정의된 모든 서비스 시작:

`docker compose up`

- 서비스를 백그라운드(분리 모드)에서 실행:

`docker compose up {{[-d|--detach]}}`

- 서비스를 시작하기 전에 이미지 다시 빌드:

`docker compose up --build`

- 특정 서비스만 실행:

`docker compose up {{서비스1 서비스2 ...}}`

- 사용자 정의 Compose 파일을 사용하여 서비스 실행:

`docker compose {{[-f|--file]}} {{경로/대상/구성파일}} up`

- 서비스를 시작하면서 고아 컨테이너 제거:

`docker compose up --remove-orphans`

- 서비스 인스턴스 수를 조정하여 실행:

`docker compose up --scale {{서비스}}={{개수}}`

- 타임스탬프와 함께 로그를 출력하며 서비스 실행:

`docker compose up --timestamps`
