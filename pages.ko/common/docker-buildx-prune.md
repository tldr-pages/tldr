# docker buildx prune

> 빌드 캐시를 제거.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/buildx/prune/>.

- 현재 활성 빌더의 빌드 캐시 제거:

`docker buildx prune`

- 특정 필터 조건에 따라 캐시 레코드 제거:

`docker buildx prune --filter "{{type=source.local}}"`

- 캐시 크기와 지정한 값 이하가 될 때까지 오래된 캐시 제거:

`docker buildx prune --max-used-space {{128mb}}`

- 지정한 여유 디스크 공간이 확보될 때까지 오래된 캐시 제거:

`docker buildx prune --reserved-space {{2gb}}`
