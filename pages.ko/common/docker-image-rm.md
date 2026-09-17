# docker image rm

> Docker 이미지를 삭제.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- 이름으로 하나 이상의 이미지 삭제:

`docker {{[rmi|image rm]}} {{이미지1 이미지2 ...}}`

- 이미지를 강제로 삭제:

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{이미지}}`

- 태그가 없는 부모 이미지는 삭제하지 않고 이미지 제거:

`docker {{[rmi|image rm]}} --no-prune {{이미지}}`

- 도움말 표시:

`docker {{[rmi|image rm]}} --help`
