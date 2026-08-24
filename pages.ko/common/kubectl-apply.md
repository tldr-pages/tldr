# kubectl apply

> Kubernetes 리소스를 정의한 파일을 통해 애플리케이션 관리.
> 클러스터에 리소스 생성 및 업데이트.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/>.

- 파일로부터 리소스 설정 적용:

`kubectl apply {{[-f|--filename]}} {{경로/대상/파일}}`

- 디렉터리의 `kustomization.yaml`을 사용하여 리소스 설정 적용:

`kubectl apply {{[-k|--kustomize]}} {{경로/대상/디렉터리}}`

- `stdin`으로부터 리소스 설정 적용:

`{{cat pod.json}} | kubectl apply {{[-f|--filename]}} -`

- 기본 편집기로 리소스의 최신 last-applied-configuration annotation 편집:

`kubectl apply edit-last-applied {{[-f|--filename]}} {{경로/대상/파일}}`

- 파일 내용과 일치하도록 last-applied-configuration annotation 설정:

`kubectl apply set-last-applied {{[-f|--filename]}} {{경로/대상/파일}}`

- 리소스 또는 파일의 최신 last-applied-configuration annotation 조회:

`kubectl apply view-last-applied {{[-f|--filename]}} {{경로/대상/파일}}`
