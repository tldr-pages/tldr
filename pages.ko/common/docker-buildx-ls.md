# docker buildx ls

> 빌더 인스턴스와 연결된 노드 목록을 출력.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/buildx/ls/>.

- 빌더 인스턴스 목록 출력:

`docker buildx ls`

- Go 템플릿으로 출력 형식 지정:

`docker buildx ls --format "{{.NAME}}: {{.DriverEndpoint}}"`
