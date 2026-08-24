# kubectl top

> Kubernetes 노드 또는 Pod의 리소스 사용량 조회.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/>.

- 모든 노드의 리소스 사용량 조회:

`kubectl top {{[no|nodes]}}`

- 특정 노드의 리소스 사용량 조회:

`kubectl top {{[no|nodes]}} {{노드_이름}}`

- 모든 Pod의 리소스 사용량 조회:

`kubectl top {{[po|pods]}}`

- 특정 Pod의 리소스 사용량 조회:

`kubectl top {{[po|pods]}} {{pod_이름}}`

- 특정 네임스페이스의 모든 Pod 리소스 사용량 조회:

`kubectl top {{[po|pods]}} {{[-n|--namespace]}} {{네임스페이스_이름}}`

- Pod 내 모든 컨테이너의 리소스 사용량 조회:

`kubectl top {{[po|pods]}} --containers`

- 특정 라벨을 가진 Pod들의 리소스 사용량 조회:

`kubectl top {{[po|pods]}} {{[-l|--selector]}} {{키=값}}`
