# docker context

> 여러 Docker 환경을 관리하기 위해 컨텍스트를 전환.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/context/>.

- 특정 Docker 엔드포인트를 사용하여 컨텍스트 생성:

`docker context create {{컨텍스트_이름}} --docker "host={{tcp://remote-host:2375}}"`

- `$DOCKER_HOST` 환경 변수를 기반으로 컨텍스트 생성:

`docker context create {{컨텍스트_이름}}`

- 컨텍스트 전환:

`docker context use {{컨텍스트_이름}}`

- 모든 컨텍스트 목록 출력:

`docker context ls`
