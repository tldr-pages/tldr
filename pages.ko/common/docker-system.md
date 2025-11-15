# docker system

> Docker 데이터를 관리하고 시스템 전반의 정보를 표시합니다.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/system/>.

- 도움말 표시:

`docker system`

- Docker 디스크 사용량 표시:

`docker system df`

- 디스크 사용량에 대한 자세한 정보 표시:

`docker system df {{[-v|--verbose]}}`

- 사용하지 않는 데이터 제거:

`docker system prune`

- 지정된 시간 이상 전에 생성된 사용하지 않는 데이터 제거:

`docker system prune --filter "until={{hours}}h{{minutes}}m"`

- Docker 데몬의 실시간 이벤트 표시:

`docker system events`

- 유효한 JSON 라인으로 스트리밍되는 컨테이너의 실시간 이벤트 표시:

`docker system events {{[-f|--filter]}} 'type=container' --format '{{json .}}'`

- 시스템 전반의 정보 표시:

`docker system info`
