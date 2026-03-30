# docker search

> Docker Hub에서 Docker 이미지를 검색.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/search/>.

- 이름 또는 키워드로 Docker 이미지 검색:

`docker search {{키워드}}`

- 공식 이미지만 필터링하여 검색:

`docker search {{[-f|--filter]}} is-official=true {{키워드}}`

- 자동 빌드 이미지만 필터링하여 검색:

`docker search {{[-f|--filter]}} is-automated=true {{키워드}}`

- 최소 별점 기준으로 이미지 검색:

`docker search {{[-f|--filter]}} stars={{number}} {{키워드}}`

- 검색 결과 개수 제한:

`docker search --limit {{number}} {{키워드}}`

- 출력 형식 커스터마이징:

`docker search {{[-f|--format]}} "{{.Name}}: {{.Description}}" {{키워드}}`
