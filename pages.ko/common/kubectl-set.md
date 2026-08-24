# kubectl set

> 기존 애플리케이션 리소스의 특정 필드 업데이트.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/>.

- Deployment의 특정 컨테이너 이미지 변경:

`kubectl set image {{[deploy|deployment]}}/{{deployment_이름}} {{컨테이너_이름}}={{이미지}}`

- Deployment의 모든 컨테이너 이미지 변경:

`kubectl set image {{[deploy|deployment]}}/{{deployment_이름}} *={{이미지}}`

- Deployment의 CPU 및 메모리 리소스 제한 설정:

`kubectl set resources {{[deploy|deployment]}}/{{deployment_이름}} --limits cpu={{cpu_제한}},memory={{메모리_제한}}`

- Deployment에 환경 변수 추가 또는 수정:

`kubectl set env {{[deploy|deployment]}}/{{deployment_이름}} {{변수_이름}}={{값}}`

- Deployment에서 환경 변수 제거:

`kubectl set env {{[deploy|deployment]}}/{{deployment_이름}} {{변수_이름}}-`

- Secret 또는 ConfigMap으로부터 환경 변수 가져오기:

`kubectl set env --from {{secret|configmap}}/{{리소스_이름}} {{[deploy|deployment]}}/{{deployment_이름}}`

- Deployment의 ServiceAccount 변경:

`kubectl set {{[sa|serviceaccount]}} {{[deploy|deployment]}}/{{deployment_이름}} {{service_account_이름}}`
