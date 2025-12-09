# kubectl apply

> Kubernetes 리소스를 정의하는 파일을 통해 애플리케이션을 관리하세요.
> 클러스터에서 리소스를 생성하고 업데이트하세요.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply>.

- 파일 이름이나 `stdin`으로 리소스에 설정 적용:

`kubectl apply {{[-f|--filename]}} {{리소스_파일명}}`

- 기본 편집기를 사용하여 리소스의 최신 마지막 적용 구성 주석 수정:

`kubectl apply edit-last-applied {{[-f|--filename]}} {{리소스_파일명}}`

- 파일 내용과 일치하도록 설정하여 최신 마지막 적용 구성 주석 설정:

`kubectl apply set-last-applied {{[-f|--filename]}} {{리소스_파일명}}`

- 유형/이름 또는 파일로 최신 마지막 적용 구성 주석 보기:

`kubectl apply view-last-applied {{[-f|--filename]}} {{리소스_파일명}}`
