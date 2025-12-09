# kubectl run

> Kubernetes에서 파드를 실행. 일부 K8S 버전에서 경고 메시지를 피하기 위해 파드 생성기를 지정.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_run>.

- nginx 파드를 실행하고 포트 80을 노출:

`kubectl run {{nginx-dev}} --image nginx --port 80`

- TEST_VAR 환경 변수를 설정하여 nginx 파드 실행:

`kubectl run {{nginx-dev}} --image nginx --env "{{TEST_VAR}}={{testing}}"`

- nginx 컨테이너를 생성하기 위해 수행될 API 호출을 표시:

`kubectl run {{nginx-dev}} --image nginx --dry-run={{none|server|client}}`

- Ubuntu 파드를 대화형으로 실행, 재시작하지 않으며 종료 시 제거:

`kubectl run {{temp-ubuntu}} --image ubuntu:22.04 --restart Never --rm -- /bin/bash`

- 기본 명령을 echo로 변경하고 사용자 정의 인수를 지정하여 Ubuntu 파드 실행:

`kubectl run {{temp-ubuntu}} --image ubuntu:22.04 --command -- echo {{인수1 인수2 ...}}`
