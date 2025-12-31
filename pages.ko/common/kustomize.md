# kustomize

> Kubernetes 리소스를 쉽게 배포.
> 더 많은 정보: <https://github.com/kubernetes-sigs/kustomize/blob/master/site/content/en/docs/Reference/CLI/_index.md>.

- 리소스 및 네임스페이스가 포함된 커스터마이제이션 파일 생성:

`kustomize create --resources {{deployment.yaml,service.yaml}} --namespace {{staging}}`

- 커스터마이제이션 파일을 빌드하고 `kubectl`로 배포:

`kustomize build . | kubectl apply -f -`

- 커스터마이제이션 파일에 이미지 설정:

`kustomize edit set image {{busybox=alpine:3.6}}`

- 현재 디렉터리의 Kubernetes 리소스를 검색하여 커스터마이제이션 파일에 추가:

`kustomize create --autodetect`
