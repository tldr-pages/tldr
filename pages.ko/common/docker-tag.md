# docker tag

> 기존 Docker 이미지에 태그를 지정합니다.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/tag/>.

- 특정 이미지 ID에 이름과 태그 지정:

`docker tag {{id}} {{이름}}:{{태그}}`

- 특정 이미지에 태그 지정:

`docker tag {{이미지}}:{{현재_태그}} {{이미지}}:{{새_태그}}`

- 도움말 표시:

`docker tag`
