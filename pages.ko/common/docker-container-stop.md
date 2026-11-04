# docker container stop

> 하나 이상의 실행 중인 컨테이너를 중지.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/stop/>.

- Docker 컨테이너 중지:

`docker {{[stop|container stop]}} {{컨테이너}}`

- 지정한 시그널을 전송하여 컨테이너 중지:

`docker {{[stop|container stop]}} {{[-s|--signal]}} {{시그널}} {{컨테이너}}`

- 지정한 시간(초) 동안 대기한 후 강제로 컨테이너 종료:

`docker {{[stop|container stop]}} {{[-t|--timeout]}} {{초}} {{컨테이너}}`

- 하나 이상의 컨테이너 중지:

`docker {{[stop|container stop]}} {{컨테이너1 컨테이너2 ...}}`

- 도움말 표시:

`docker {{[stop|container stop]}} --help`
