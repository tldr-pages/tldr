# kubectl debug

> 대화형 디버깅 컨테이너를 사용하여 Kubernetes 클러스터 리소스 디버깅.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_debug/>.

- Pod에 대화형 디버그 세션을 생성하고 즉시 연결:

`kubectl debug {{pod_이름}} {{[-it|--stdin --tty]}} --image busybox`

- 사용자 지정 이미지와 컨테이너 이름으로 디버그 컨테이너 생성:

`kubectl debug --image {{image}} {{[-c|--container]}} {{컨테이너_이름}} {{pod_이름}}`

- 노드에 대화형 디버그 세션을 생성하고 즉시 연결 (컨테이너는 호스트 네임스페이스 사용 및 파일시스템은 `/host`에 마운트):

`kubectl debug node/{{노드_이름}} {{[-it|--stdin --tty]}} --image busybox`

- Pod 복사본을 생성하고 디버그 컨테이너 추가:

`kubectl debug {{pod_이름}} {{[-it|--stdin --tty]}} --image {{image}} --copy-to {{pod_복사본_이름}}`

- Pod 복사본을 생성하고 특정 컨테이너의 실행 명령 변경:

`kubectl debug {{pod_이름}} {{[-it|--stdin --tty]}} --copy-to {{pod_복사본_이름}} --container {{컨테이너_이름}} -- {{명령어}}`

- Pod 복사본을 생성하고 특정 컨테이너 이미지 변경:

`kubectl debug {{pod_이름}} --copy-to {{pod_복사본_이름}} --set-image {{컨테이너_이름}}={{이미지}}`

- Pod 복사본을 생성하고 모든 컨테이너 이미지 변경:

`kubectl debug {{pod_이름}} --copy-to {{pod_복사본_이름}} --set-image '*={{이미지}}'`

- 특정 컨테이너를 대상으로 임시 디버그 컨테이너 생성 (distroless 컨테이너 디버깅에 유리):

`kubectl debug {{pod_이름}} {{[-it|--stdin --tty]}} --image {{이미지}} --target {{대상_컨테이너_이름}}`
