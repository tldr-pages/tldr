# kubectl plugin

> kubectl 기능을 확장하는 플러그인 관리.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_plugin/>.

- 시스템의 `$PATH`에서 사용 가능한 모든 플러그인 목록 표시:

`kubectl plugin list`

- 전체 경로 없이 플러그인 실행 파일 이름만 표시:

`kubectl plugin list --name-only`

- 도움말 표시:

`kubectl plugin {{[-h|--help]}}`
