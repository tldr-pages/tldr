# eksctl

> Amazon EKS의 공식 CLI.
> 더 많은 정보: <https://eksctl.io>.

- 기본 클러스터 생성:

`eksctl create cluster`

- 클러스터 또는 모든 클러스터에 대한 세부 정보를 나열:

`eksctl get cluster --name={{이름}} --region={{지역}}`

- 파일의 모든 구성 정보를 전달하는 클러스터를 생성:

`eksctl create cluster --config-file={{경로/대상/파일}}`

- 구성 파일을 사용하여 클러스터를 생성하고, 나중에까지 노드 그룹 생성을 건너뜀:

`eksctl create cluster --config-file=<path> --without-nodegroup`

- 클러스터 삭제:

`eksctl delete cluster --name={{이름}} --region={{지역}}`

- 클러스터를 생성하고, 기본값이 아닌 다른 파일에 클러스터 자격 증명을 사용:

`eksctl create cluster --name={{이름}} --nodes={{4}} --kubeconfig={{path/to/config.yaml}}`

- 클러스터를 생성하고, 클러스터 자격 증명을 로컬에 저장하지 않도록 방지:

`eksctl create cluster --name={{이름}} --nodes={{4}} --write-kubeconfig=false`

- 클러스터를 생성하고 `eksctl`이 `~/.kube/eksctl/clusters` 디렉터리에서 클러스터 자격 증명을 관리:

`eksctl create cluster --name={{이름}} --nodes={{4}} --auto-kubeconfig`
