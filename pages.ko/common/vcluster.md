# vcluster

> 네임스페이스 내에서 경량 가상 Kubernetes 클러스터를 생성하고 관리.
> 더 많은 정보: <https://www.vcluster.com/docs/vcluster>.

- 지정한 네임스페이스에 가상 클러스터 생성:

`vcluster create {{vcluster_이름}} {{[-n|--namespace]}} {{네임스페이스}}`

- 로컬 포트와 Insecure 모드를 사용하여 가상 클러스터에 연결:

`vcluster connect {{vcluster_이름}} {{[-n|--namespace]}} {{네임스페이스}} --local-port {{port}} --insecure`

- 모든 가상 클러스터 목록 표시:

`vcluster list`

- 가상 클러스터 삭제:

`vcluster delete {{vcluster_이름}}`

- 플랫폼에서 관리하는 가상 클러스터 목록 표시:

`vcluster platform list`

- 플랫폼에서 관리하는 가상 클러스터 생성:

`vcluster platform create {{vcluster_이름}} {{[-n|--namespace]}} {{네임스페이스}}`

- 플랫폼에서 관리하는 가상 클러스터에 연결:

`vcluster platform connect {{vcluster_이름}} {{[-n|--namespace]}} {{네임스페이스}}`

- 플랫폼에서 관리하는 가상 클러스터 삭제:

`vcluster platform delete {{vcluster_이름}} {{[-n|--namespace]}} {{네임스페이스}}`
