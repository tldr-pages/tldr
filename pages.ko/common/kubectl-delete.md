# kubectl delete

> Kubernetes 리소스 삭제.
> 더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

- 특정 포드 삭제:

`kubectl delete pod {{포드_이름}}`

- 특정 배포 삭제:

`kubectl delete deployment {{배포_이름}}`

- 특정 노드 삭제:

`kubectl delete node {{노드_이름}}`

- 지정된 네임스페이스의 모든 포드 삭제:

`kubectl delete pods --all --namespace {{네임스페이스}}`

- 지정된 네임스페이스의 모든 배포 및 서비스 삭제:

`kubectl delete deployments,services --all --namespace {{네임스페이스}}`

- 모든 노드 삭제:

`kubectl delete nodes --all`

- YAML 매니페스트에 정의된 리소스 삭제:

`kubectl delete --filename {{경로/대상/매니페스트.yaml}}`
