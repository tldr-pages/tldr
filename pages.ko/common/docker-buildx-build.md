# docker buildx build

> BuildKit 엔진을 사용하여 Dockerfile에서 이미지를 빌드.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/buildx/build>.

- 현재 디렉터리의 Dockerfile을 사용하여 이미지 빌드:

`docker buildx build .`

- 이미지를 빌드하고 태그 지정:

`docker buildx build {{[-t|--tag]}} {{이미지:태그}} .`

- 지정한 Dockerfile을 사용하여 이미지 빌드:

`docker buildx build {{[-f|--file]}} {{경로/대상/Dockerfile}} .`

- 빌드 시 사용할 변수를 전달하여 이미지 빌드:

`docker buildx build --build-arg {{HTTP_PROXY=http://proxy.example.com}} --build-arg {{VERSION=1.0}} .`

- 빌드 캐시를 사용하지 않고 이미지 빌드:

`docker buildx build --no-cache .`

- 이미지를 빌드하고 `docker images`에 로드:

`docker buildx build --load {{[-t|--tag]}} {{이미지:태그}} .`

- 여러 플랫폼용 이미지를 빌드하고 레지스트리에 푸시:

`docker buildx build --platform {{linux/amd64,linux/arm64}} --push {{[-t|--tag]}} {{registry.example.com/이미지:태그}} .`

- 멀티 스테이지 Dockerfile에서 지정한 스테이지만 빌드:

`docker buildx build --target {{스테이지_이름}} {{[-t|--tag]}} {{이미지:태그}} .`
