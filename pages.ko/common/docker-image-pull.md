# docker pull

> Docker 이미지를 레지스트리에서 다운로드.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- 특정 Docker 이미지 다운로드:

`docker pull {{이미지}}:{{태그}}`

- 조용한 모드로 특정 Docker 이미지 다운로드:

`docker pull {{[-q|--quiet]}} {{이미지}}:{{태그}}`

- 특정 Docker 이미지의 모든 태그 다운로드:

`docker pull {{[-a|--all-tags]}} {{이미지}}`

- 특정 플랫폼의 Docker 이미지 다운로드 (예: linux/amd64):

`docker pull --platform {{linux/amd64}} {{이미지}}:{{태그}}`

- 도움말 표시:

`docker pull {{[-h|--help]}}`
