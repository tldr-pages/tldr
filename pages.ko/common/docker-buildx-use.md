# docker buildx use

> 현재 사용할 빌더 인스턴스를 설정.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/buildx/use>.

- 지정한 빌더 인스턴스를 현재 빌더로 설정:

`docker buildx use {{빌더_이름}}`

- 빌더를 현재 컨텍스트의 기본 빌더로 설정:

`docker buildx use --default {{빌더_이름}}`

- 빌더를 전역으로 설정하여 컨텍스트 간에도 설정 유지:

`docker buildx use --global {{빌더_이름}}`
