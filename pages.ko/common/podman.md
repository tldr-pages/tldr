# podman

> 파드, 컨테이너 및 이미지의 간단한 관리 도구.
> Podman은 Docker-CLI와 유사한 명령줄을 제공합니다. 간단히 말해: `alias docker=podman`.
> 더 많은 정보: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- 모든 컨테이너 나열 (실행 중 및 중지됨 모두 포함):

`podman ps --all`

- 이미지에서 사용자 정의 이름으로 컨테이너 생성:

`podman run --name {{컨테이너_이름}} {{이미지}}`

- 기존 컨테이너 시작 또는 중지:

`podman {{start|stop}} {{컨테이너_이름}}`

- 레지스트리에서 이미지 가져오기 (기본은 Docker Hub):

`podman pull {{이미지}}`

- 이미 다운로드된 이미지 목록 표시:

`podman images`

- 이미 실행 중인 컨테이너 안에서 셸 열기:

`podman exec --interactive --tty {{컨테이너_이름}} {{sh}}`

- 중지된 컨테이너 제거:

`podman rm {{컨테이너_이름}}`

- 하나 이상의 컨테이너 로그 출력 및 실시간 로그 추적:

`podman logs --follow {{컨테이너_이름}} {{컨테이너_ID}}`
