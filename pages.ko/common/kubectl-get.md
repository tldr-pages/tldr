# kubectl get

> Kubernetes 객체 및 리소스 가져오기.
> 더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- 현재 클러스터의 모든 네임스페이스 가져오기:

`kubectl get namespaces`

- 지정된 [n]amespace의 노드 가져오기:

`kubectl get nodes --namespace {{네임스페이스}}`

- 지정된 [n]amespace의 파드 가져오기:

`kubectl get pods --namespace {{네임스페이스}}`

- 지정된 [n]amespace의 배포 가져오기:

`kubectl get deployments --namespace {{네임스페이스}}`

- 지정된 [n]amespace의 서비스 가져오기:

`kubectl get services --namespace {{네임스페이스}}`

- 지정된 [n]amespace의 모든 리소스 가져오기:

`kubectl get all --namespace {{네임스페이스}}`

- YAML 매니페스트 [f]ile에 정의된 Kubernetes 객체 가져오기:

`kubectl get --file {{경로/대상/매니페스트.yaml}}`
