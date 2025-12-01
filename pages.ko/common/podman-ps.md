# podman ps

> Podman 컨테이너 목록을 나열합니다.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- 현재 실행 중인 Podman 컨테이너 나열:

`podman ps`

- 모든 Podman 컨테이너 나열 (실행 중 및 중지된 컨테이너 포함):

`podman ps {{[-a|--all]}}`

- 가장 최근에 생성된 컨테이너 표시 (모든 상태 포함):

`podman ps {{[-l|--latest]}}`

- 이름에 특정 문자열이 포함된 컨테이너 필터링:

`podman ps {{[-f|--filter]}} "name={{이름}}"`

- 주어진 이미지를 조상으로 공유하는 컨테이너 필터링:

`podman ps {{[-f|--filter]}} "ancestor={{이미지}}:{{태그}}"`

- 종료 상태 코드로 컨테이너 필터링:

`podman ps {{[-af|--all --filter]}} "exited={{코드}}"`

- 상태별로 컨테이너 필터링 (생성됨, 실행 중, 제거 중, 일시 중지됨, 종료됨, 죽은 상태):

`podman ps {{[-f|--filter]}} "status={{상태}}"`

- 특정 볼륨을 마운트했거나 특정 경로에 볼륨이 마운트된 컨테이너 필터링:

`podman ps {{[-f|--filter]}} "volume={{경로/대상/폴더}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
