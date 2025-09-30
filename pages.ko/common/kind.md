# kind

> Docker 컨테이너 "노드"를 사용하여 로컬 Kubernetes 클러스터를 실행.
> Kubernetes 자체 테스트를 위해 설계되었으나, 로컬 개발이나 지속적 통합에도 사용 가능.
> 더 많은 정보: <https://github.com/kubernetes-sigs/kind>.

- 로컬 Kubernetes 클러스터 생성:

`kind create cluster --name {{클러스터_이름}}`

- 하나 이상의 클러스터 삭제:

`kind delete clusters {{클러스터_이름}}`

- 클러스터, 노드 또는 kubeconfig에 대한 세부 정보 가져오기:

`kind get {{clusters|nodes|kubeconfig}}`

- kubeconfig 또는 로그 내보내기:

`kind export {{kubeconfig|logs}}`
