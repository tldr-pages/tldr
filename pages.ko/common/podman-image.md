# podman image

> Docker 이미지 관리.
> 같이 보기: `podman build`, `podman import`, `podman pull`.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- 로컬 Docker 이미지 나열:

`podman image ls`

- 사용되지 않는 로컬 Docker 이미지 삭제:

`podman image prune`

- 모든 사용되지 않는 이미지 삭제 (태그가 없는 이미지뿐만 아니라):

`podman image prune --all`

- 로컬 Docker 이미지의 히스토리 표시:

`podman image history {{이미지}}`
