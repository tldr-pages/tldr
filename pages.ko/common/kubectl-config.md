# kubectl config

> Kubernetes 구성(kubeconfig) 파일을 관리하여 `kubectl` 또는 Kubernetes API를 통해 클러스터에 접근할 수 있도록 함.
> 기본적으로 Kubernetes는 `${HOME}/.kube/config`에서 구성을 가져옵니다.
> 같이 보기: `kubectx`, `kubens`.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config>.

- 기본 kubeconfig 파일에서 모든 컨텍스트 가져오기:

`kubectl config get-contexts`

- 사용자 지정 kubeconfig 파일에서 모든 클러스터/컨텍스트/사용자 가져오기:

`kubectl config {{get-clusters|get-contexts|get-users}} --kubeconfig {{경로/대상/kubeconfig.yaml}}`

- 현재 컨텍스트 가져오기:

`kubectl config current-context`

- 다른 컨텍스트로 전환:

`kubectl config {{use|use-context}} {{컨텍스트_이름}}`

- 클러스터/컨텍스트/사용자 삭제:

`kubectl config {{delete-cluster|delete-context|delete-user}} {{cluster|context|user}}`

- 사용자 지정 kubeconfig 파일을 영구적으로 추가:

`export KUBECONFIG="{{$HOME.kube/config:경로/대상/사용자/정의/kubeconfig.yaml}}" kubectl config get-contexts`
