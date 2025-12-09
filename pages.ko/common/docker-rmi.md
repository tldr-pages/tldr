# docker rmi

> Docker 이미지 삭제.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- 도움말 표시:

`docker rmi`

- 하나 이상의 이미지를 이름으로 삭제:

`docker rmi {{이미지1 이미지2 ...}}`

- 강제로 이미지 삭제:

`docker rmi {{[-f|--force]}} {{이미지}}`

- 태그되지 않은 부모 이미지를 삭제하지 않고 이미지 삭제:

`docker rmi --no-prune {{이미지}}`
