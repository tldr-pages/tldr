# talosctl

> 최소 구성 및 불변 방식의 Kubernetes 배포판인 Talos Linux와 상호작용.
> 관련 항목: `kubectl`.
> 더 많은 정보: <https://docs.siderolabs.com/talos/v1.11/reference/cli>.

- 새로운 노드에 설정을 적용:

`talosctl apply-config {{[-i|--insecure]}} {{[-n|--nodes]}} {{컨트롤_플레인_ip}} {{[-f|--file]}} {{경로/대상/컨트롤_플레인.yaml}}`

- 노드에서 `etcd` 클러스터 부트스트랩:

`talosctl bootstrap {{[-n|--nodes]}} {{node_ip}}`

- API 리소스 편집:

`talosctl edit {{편집할_리소스}} {{[-n|--nodes]}} {{노드_ip}}`

- 리소스 조회:

`talosctl get {{가져올_리소스}} {{[-n|--nodes]}} {{노드_ip}}`

- 노드에서 관리자용 kube 구성 다운로드:

`talosctl kubeconfig {{[-n|--nodes]}} {{노드_ip}}`

- 노드 초기화:

`talosctl reset {{[-n|--nodes]}} {{노드_ip}}`
