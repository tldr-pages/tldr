# kubectl api-resources

> Kubernetes API 서버가 지원하는 API 리소스 목록 출력.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-resources/>.

- 지원되는 API 리소스 목록 출력:

`kubectl api-resources`

- 추가 정보를 포함하여 API 리소스 목록 출력:

`kubectl api-resources {{[-o|--output]}} wide`

- 특정 컬럼 기준으로 API 리소스 정렬 출력:

`kubectl api-resources --sort-by {{이름}}`

- 네임스페이스에 속하는 리소스만 출력:

`kubectl api-resources --namespaced`

- 네임스페이스에 속하지 않는 리소스만 출력:

`kubectl api-resources --namespaced=false`

- 특정 API 그룹에 속하는 API 리소스만 출력:

`kubectl api-resources --api-group {{api_그룹}}`
