# gcloud components install

> Google Cloud CLI의 구성 요소와 그 의존성을 설치.
> 기존 설치를 업그레이드하지 않고 현재 Google Cloud CLI 버전의 구성 요소를 설치.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/components/install>.

- 설치 가능한 구성 요소 보기:

`gcloud components list`

- 하나 이상의 구성 요소 설치 (필요한 의존성도 함께 설치):

`gcloud components install {{구성_요소_id1 구성_요소_id2 ...}}`

- 현재 Google Cloud CLI 버전 확인:

`gcloud version`

- Google Cloud CLI를 최신 버전으로 업데이트:

`gcloud components update`
