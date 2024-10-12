# docker-slim

> Docker 이미지를 분석하고 최적화.
> 더 많은 정보: <https://github.com/slimtoolkit/slim>.

- 인터랙티브 모드로 DockerSlim 시작:

`docker-slim`

- 특정 이미지에서 Docker 레이어 분석:

`docker-slim xray --target {{이미지:태그}}`

- Dockerfile 검사:

`docker-slim lint --target {{경로/대상/Dockerfile}}`

- 분석하고 최적화된 Docker 이미지 생성:

`docker-slim build {{이미지:태그}}`

- 하위 명령에 대한 도움말 표시:

`docker-slim {{하위_명령}} --help`
