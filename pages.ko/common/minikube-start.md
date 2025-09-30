# minikube start

> 다양한 설정으로 `minikube` 시작.
> 더 많은 정보: <https://minikube.sigs.k8s.io/docs/commands/start/>.

- 특정 Kubernetes 버전으로 `minikube` 시작:

`minikube start --kubernetes-version {{v1.24.0}}`

- 특정 자원 할당(예: 메모리 및 CPU)으로 `minikube` 시작:

`minikube start --memory {{2048}} --cpus {{2}}`

- 특정 드라이버(예: VirtualBox)로 `minikube` 시작:

`minikube start --driver {{virtualbox}}`

- 백그라운드에서 `minikube` 시작 (헤드리스 모드):

`minikube start --background`

- 사용자 지정 애드온(예: 메트릭 서버)과 함께 `minikube` 시작:

`minikube start --addons {{metrics-server}}`
