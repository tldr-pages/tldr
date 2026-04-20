# docker buildx du

> 빌더의 디스크 사용량을 확인.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/buildx/du/>.

- 디스크 사용량 출력:

`docker buildx du`

- 특정 조건으로 출력 필터링:

`docker buildx du --filter "{{description~=golang}}"`

- 상세 출력:

`docker buildx du --verbose`

- Go 템플릿으로 출력 형식 지정:

`docker buildx du --format "table {{.ID}}    {{.Description}}"`

- `jq`를 사용해 JSON 형식으로 보기 좋게 출력:

`docker buildx du --format json | jq .`

- 특정 빌더의 디스크 사용량 확인:

`docker buildx du --builder {{빌더_이름}}`
