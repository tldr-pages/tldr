# kubectl cluster-info

> Kubernetes 마스터와 클러스터 서비스의 엔드포인트 정보 표시.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cluster-info/>.

- 기본 클러스터 정보 표시:

`kubectl cluster-info`

- 현재 클러스터 상태를 `stdout`으로 출력 (디버깅용):

`kubectl cluster-info dump`

- 클러스터 상태를 디렉터리에 저장:

`kubectl cluster-info dump --output-directory {{경로/대상/디렉터리}}`

- 특정 kubeconfig 컨텍스트를 사용해 클러스터 정보 표시:

`kubectl cluster-info --context {{컨텍스트_이름}}`
