# docker buildx rm

> 하나 이상의 빌더 인스턴스를 제거.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/buildx/rm/>.

- 빌더 인스턴스 제거:

`docker buildx rm {{빌더_이름}}`

- 모든 비활성 빌더 제거:

`docker buildx rm --all-inactive`

- 확인 없이 모든 비활성 빌더 강제 제거:

`docker buildx rm --all-inactive {{[-f|--force]}}`
