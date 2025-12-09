# gcloud

> Google Cloud Platform을 위한 공식 CLI 도구.
> 참고: `gcloud` 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud>.

- 활성 구성에서 모든 속성 나열:

`gcloud config list`

- Google 계정에 로그인:

`gcloud auth login`

- 활성 프로젝트 설정:

`gcloud config set project {{프로젝트_이름}}`

- 가상 머신 인스턴스에 SSH 접속:

`gcloud compute ssh {{사용자}}@{{인스턴스}}`

- 프로젝트 내 모든 Google Compute Engine 인스턴스 표시 (기본적으로 모든 영역의 인스턴스가 나열됨):

`gcloud compute instances list`

- 적절한 자격 증명으로 kubeconfig 파일을 업데이트하여 `kubectl`을 특정 Google Kubernetes Engine (GKE) 클러스터에 연결:

`gcloud container clusters get-credentials {{클러스터_이름}}`

- 모든 `gcloud` 구성 요소 업데이트:

`gcloud components update`

- 특정 명령에 대한 도움말 표시:

`gcloud help {{명령}}`
