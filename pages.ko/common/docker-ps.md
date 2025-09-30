# docker ps

> Docker 컨테이너 목록.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- 현재 실행 중인 Docker 컨테이너 목록:

`docker ps`

- 모든 Docker 컨테이너 목록 (실행 중 및 중지됨):

`docker ps {{[-a|--all]}}`

- 가장 최근에 생성된 컨테이너 표시 (모든 상태 포함):

`docker ps {{[-l|--latest]}}`

- 이름에 특정 문자열이 포함된 컨테이너 필터링:

`docker ps {{[-f|--filter]}} "name={{이름}}"`

- 주어진 이미지를 조상으로 공유하는 컨테이너 필터링:

`docker ps {{[-f|--filter]}} "ancestor={{이미지}}:{{태그}}"`

- 종료 상태 코드로 컨테이너 필터링:

`docker ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{코드}}"`

- 상태로 컨테이너 필터링 (created, running, removing, paused, exited, dead):

`docker ps {{[-f|--filter]}} "status={{상태}}"`

- 특정 볼륨을 마운트하거나 특정 경로에 볼륨이 마운트된 컨테이너 필터링:

`docker ps {{[-f|--filter]}} "volume={{경로/대상/폴더}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
