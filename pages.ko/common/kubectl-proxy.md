# kubectl proxy

> localhost와 Kubernetes API 서버 사이에 프록시 서버 또는 애플리케이션 레벨 게이트웨이 생성.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_proxy/>.

- 기본 설정(포트 8001, localhost 바인딩)으로 프록시 실행:

`kubectl proxy`

- 로컬 정적 파일을 제공하면서 Kubernetes API 일부를 프록시:

`kubectl proxy {{[-w|--www]}} {{경로/대상/정적_디렉토리}} {{[-P|--www-prefix]}} {{/static_prefix/}} --api-prefix {{/api_서브셋/}}`

- Kubernetes API 전체를 사용자 지정 URL 접두사 아래로 프록시:

`kubectl proxy --api-prefix {{/custom_prefix/}}`

- 특정 포트에서 Kubernetes API와 정적 콘텐츠를 함께 제공:

`kubectl proxy {{[-p|--port]}} {{포트}} {{[-w|--www]}} {{경로/대상/정적_디렉토리}}`

- 임의의 로컬 포트로 프록시 실행하고, 선택된 포트를 `stdout`로 출력:

`kubectl proxy {{[-p|--port]}} 0`

- TCP 포트 대신 Unix Domain Socket으로 프록시 실행:

`kubectl proxy {{[-u|--unix-socket]}} {{경로/대상/소켓}}`

- 모든 네트워크 인터페이스에서 연결 허용 (프록시를 공개할 때 주의 필요):

`kubectl proxy --address 0.0.0.0 --accept-hosts '.*'`

- 특정 API 경로만 허용하고 민감한 엔드포인트는 차단:

`kubectl proxy --accept-paths '^/api/v1/namespaces/default/.*' --reject-paths '^/api/.*/pods/.*/exec'`
