# docker load

> 파일 또는 `stdin`에서 Docker 이미지를 로드합니다.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/load/>.

- `stdin`에서 Docker 이미지 로드:

`docker load < {{경로/대상/이미지_파일.tar}}`

- 특정 파일에서 Docker 이미지 로드:

`docker load {{[-i|--input]}} {{경로/대상/이미지_파일.tar}}`

- 조용한 모드로 특정 파일에서 Docker 이미지 로드:

`docker load {{[-q|--quiet]}} {{[-i|--input]}} {{경로/대상/이미지_파일.tar}}`
