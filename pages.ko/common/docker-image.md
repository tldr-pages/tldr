# docker image

> 도커 이미지 관리.
> 관련 항목: `docker build`, `docker image pull`, `docker image rm`.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/>.

- 로컬 도커 이미지 목록 보기:

`docker {{[images|image ls]}}`

- 사용되지 않는 로컬 도커 이미지 제거:

`docker image prune`

- (태그가 없는 이미지뿐만 아니라) 모든 사용되지 않는 이미지 제거:

`docker image prune {{[-a|--all]}}`

- 특정 로컬 도커 이미지 히스토리 보기:

`docker {{[history|image history]}} {{이미지}}`
