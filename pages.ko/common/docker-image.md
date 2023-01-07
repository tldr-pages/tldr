# docker image

> 도커 이미지 관리.
> `docker build`, `docker import`, `docker pull` 도 확인하세요.
> 더 많은 정보: <https://docs.docker.com/engine/reference/commandline/image/>.

- 로컬 도커 이미지 목록 보기:

`docker image ls`

- 사용되지 않는 로컬 도커 이미지 제거:

`docker image prune`

- (태그가 없는 이미지뿐만 아니라) 모든 사용되지 않는 이미지 제거:

`docker image prune --all`

- 특정 로컬 도커 이미지 히스토리 보기:

`docker image history {{이미지}}`
