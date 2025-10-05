# kubectl delete

> Kubernetes 리소스 삭제.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_delete>.

- 특정 포드 삭제:

`kubectl delete {{[po|pod]}} {{포드_이름}}`

- 특정 배포 삭제:

`kubectl delete {{[deploy|deployment]}} {{배포_이름}}`

- 특정 노드 삭제:

`kubectl delete {{[no|node]}} {{노드_이름}}`

- 지정된 네임스페이스의 모든 포드 삭제:

`kubectl delete {{[po|pods]}} --all {{[-n|--namespace]}} {{네임스페이스}}`

- 지정된 네임스페이스의 모든 배포 및 서비스 삭제:

`kubectl delete {{[deploy|deployment]}},{{[svc|services]}} --all {{[-n|--namespace]}} {{네임스페이스}}`

- 모든 노드 삭제:

`kubectl delete {{[no|nodes]}} --all`

- YAML 매니페스트에 정의된 리소스 삭제:

`kubectl delete {{[-f|--filename]}} {{경로/대상/매니페스트.yaml}}`
