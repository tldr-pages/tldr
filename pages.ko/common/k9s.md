# k9s

> Kubernetes 클러스터를 보고 관리.
> 더 많은 정보: <https://k9scli.io/topics/commands/>.

- kubeconfig 컨텍스트를 사용하여 클러스터 관리:

`k9s --context {{kubeconfig_컨텍스트_이름}}`

- 읽기 전용 모드로 클러스터 관리 (수정을 초래할 수 있는 모든 명령 비활성화):

`k9s --readonly --cluster {{클러스터_이름}}`

- 주어진 Kubernetes 네임스페이스를 사용하여 클러스터 관리:

`k9s --namespace {{Kubernetes_네임스페이스}} --cluster {{클러스터_이름}}`

- pod 보기로 k9s를 실행하고 디버그 로깅을 활성화하여 클러스터 관리:

`k9s --command {{pod}} --logLevel debug --cluster {{클러스터_이름}}`
