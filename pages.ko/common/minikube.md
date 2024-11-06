# minikube

> Kubernetes를 로컬에서 실행.
> 더 많은 정보: <https://minikube.sigs.k8s.io/docs/>.

- 클러스터 시작:

`minikube start`

- 클러스터의 IP 주소 가져오기:

`minikube ip`

- 노드 포트를 통해 노출된 my_service라는 서비스에 접근하고 URL 가져오기:

`minikube service {{my_service}} --url`

- 브라우저에서 Kubernetes 대시보드 열기:

`minikube dashboard`

- 실행 중인 클러스터 중지:

`minikube stop`

- 클러스터 삭제:

`minikube delete`

- LoadBalancer 서비스에 연결:

`minikube tunnel`
