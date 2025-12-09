# kubectl describe

> Kubernetes 객체 및 리소스의 세부 정보 표시.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe>.

- [n]amespace의 포드 세부 정보 표시:

`kubectl describe {{[po|pods]}} {{[-n|--namespace]}} {{네임스페이스}}`

- [n]amespace의 노드 세부 정보 표시:

`kubectl describe {{[no|nodes]}} {{[-n|--namespace]}} {{네임스페이스}}`

- [n]amespace의 특정 포드 세부 정보 표시:

`kubectl describe {{[po|pods]}} {{포드_이름}} {{[-n|--namespace]}} {{네임스페이스}}`

- [n]amespace의 특정 노드 세부 정보 표시:

`kubectl describe {{[no|nodes]}} {{노드_이름}} {{[-n|--namespace]}} {{네임스페이스}}`

- YAML 매니페스트 [f]ile에 정의된 Kubernetes 객체의 세부 정보 표시:

`kubectl describe {{[-f|--filename]}} {{경로/대상/manifest.yaml}}`
