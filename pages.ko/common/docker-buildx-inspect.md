# docker buildx inspect

> 현재 또는 지정한 빌더 인스턴스의 정보를 확인.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/buildx/inspect>.

- 현재 빌더 인스턴스 정보 표시:

`docker buildx inspect`

- 이름을 지정하여 특정 빌더 인스턴스 정보 표시:

`docker buildx inspect {{빌더_이름}}`

- 빌더가 실행 중인 상태인지 확인한 후 정보 표시:

`docker buildx inspect --bootstrap`

- 빌더 상태를 불러올 때 사용할 타임아웃 지정(기본값: 20초):

`docker buildx inspect --timeout {{초}}`
