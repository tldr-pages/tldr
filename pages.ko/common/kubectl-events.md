# kubectl events

> Kubernetes 리소스 이벤트 조회.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_events/>.

- 기본 네임스페이스의 이벤트 표시:

`kubectl events`

- 모든 네임스페이스의 이벤트 표시:

`kubectl events {{[-A|--all-namespaces]}}`

- 특정 네임스페이스의 이벤트를 실시간으로 감시:

`kubectl events {{[-w|--watch]}} {{[-n|--namespace]}} {{네임스페이스}}`

- 특정 네임스페이스의 Pod 관련 이벤트 표시:

`kubectl events --for {{pod}}/{{pod_이름}} {{[-n|--namespace]}} {{네임스페이스}}`

- 특정 네임스페이스의 리소스 관련 이벤트 표시:

`kubectl events --for {{리소스}}/{{리소스_이름}} {{[-n|--namespace]}} {{네임스페이스}}`

- `Warning` 또는 `Normal` 타입 이벤트만 표시:

`kubectl events --types Warning,Normal`

- 이벤트를 YAML 형식으로 출력:

`kubectl events {{[-o|--output]}} yaml`
