# kubectl get

> Kubernetes 객체 또는 리소스 가져오기.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/>.

- 현재 클러스터의 모든 네임스페이스 조회:

`kubectl get {{[ns|namespaces]}}`

- 특정 네임스페이스의 노드 조회:

`kubectl get {{[no|nodes]}} {{[-n|--namespace]}} {{네임스페이스}}`

- 특정 네임스페이스의 Pod 조회:

`kubectl get {{[po|pods]}} {{[-n|--namespace]}} {{네임스페이스}}`

- 특정 네임스페이스의 Deployment 조회:

`kubectl get {{[deploy|deployments]}} {{[-n|--namespace]}} {{네임스페이스}}`

- 특정 네임스페이스의 Service 조회:

`kubectl get {{[svc|services]}} {{[-n|--namespace]}} {{네임스페이스}}`

- 기타 Kubernetes 리소스 조회:

`kubectl get {{persistentvolumeclaims|secret|...}}`

- 모든 네임스페이스의 주요 리소스 조회:

`kubectl get all {{[-A|--all-namespaces]}}`

- YAML 매니페스트 파일에 정의된 Kubernetes 오브젝트 조회:

`kubectl get {{[-f|--filename]}} {{경로/대상/manifest.yaml}}`
