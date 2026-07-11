# docker buildx create

> 새로운 Buildx builder 인스턴스를 생성.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/buildx/create/>.

- 기본 Docker 컨텍스트를 사용하여 새로운 builder 인스턴스를 생성:

`docker buildx create`

- 지정한 이름으로 새로운 builder 인스턴스 생성:

`docker buildx create --name {{builder_이름}}`

- 새로운 builder 인스턴스를 생성하고 즉시 현재 활성 builder로 설정:

`docker buildx create --name {{builder_이름}} --use`

- 지정한 드라이버를 사용하여 새로운 builder 인스턴스 생성 (기본값: `docker`):

`docker buildx create --driver {{docker-container|kubernetes|remote|...}}`

- 지정한 플랫폼을 지원하는 새로운 builder 인스턴스 생성:

`docker buildx create --platform {{linux/amd64,linux/arm64,...}}`

- 기존 builder에 새 노드 추가:

`docker buildx create --name {{builder_이름}} --append {{context|endpoint}}`

- 지정한 BuildKit 데몬 옵션으로 새 builder 인스턴스 생성:

`docker buildx create --buildkitd-flags "{{--debug --debugaddr 0.0.0.0:6666}}"`

- 새로운 builder 인스턴스를 생성하고 즉시 부팅:

`docker buildx create --name {{builder_이름}} --bootstrap`
