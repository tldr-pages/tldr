# gcloud container

> Kubernetes 및 클러스터에서 컨테이너화된 애플리케이션 관리.
> 같이 보기: `gcloud`.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/container>.

- `gcloud`를 Docker 자격 증명 도우미로 등록:

`gcloud auth configure-docker`

- GKE 컨테이너를 실행할 클러스터 생성:

`gcloud container clusters create {{클러스터_이름}}`

- GKE 컨테이너를 실행할 클러스터 나열:

`gcloud container clusters list`

- `kubectl`이 GKE 클러스터를 사용하도록 kubeconfig 업데이트:

`gcloud container clusters get-credentials {{클러스터_이름}}`

- 컨테이너 이미지의 태그 및 다이제스트 메타데이터 나열:

`gcloud container images list-tags {{이미지}}`
