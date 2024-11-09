# kubectl describe

> Kubernetes 객체 및 리소스의 세부 정보 표시.
> 더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- [n]amespace의 포드 세부 정보 표시:

`kubectl describe pods --namespace {{네임스페이스}}`

- [n]amespace의 노드 세부 정보 표시:

`kubectl describe nodes --namespace {{네임스페이스}}`

- [n]amespace의 특정 포드 세부 정보 표시:

`kubectl describe pods {{포드_이름}} --namespace {{네임스페이스}}`

- [n]amespace의 특정 노드 세부 정보 표시:

`kubectl describe nodes {{노드_이름}} --namespace {{네임스페이스}}`

- YAML 매니페스트 [f]ile에 정의된 Kubernetes 객체의 세부 정보 표시:

`kubectl describe --file {{경로/대상/manifest.yaml}}`
