# doctl kubernetes cluster

> Kubernetes 클러스터를 관리하고 클러스터와 관련된 구성 옵션을 봄.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/kubernetes/cluster/>.

- Kubernetes 클러스터 생성:

`doctl kubernetes cluster create --count {{3}} --region {{nyc1}} --size {{s-1vcpu-2gb}} --version {{latest}} {{클러스터_이름}}`

- 모든 Kubernetes 클러스터 나열:

`doctl kubernetes cluster list`

- kubeconfig를 가져와 저장:

`doctl kubernetes cluster kubeconfig save {{클러스터_이름}}`

- 사용 가능한 업그레이드 확인:

`doctl kubernetes cluster get-upgrades {{클러스터_이름}}`

- 클러스터를 새로운 Kubernetes 버전으로 업그레이드:

`doctl kubernetes cluster upgrade {{클러스터_이름}}`

- 클러스터 삭제:

`doctl kubernetes cluster delete {{클러스터_이름}}`
