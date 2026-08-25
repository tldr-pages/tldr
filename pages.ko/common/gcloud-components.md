# gcloud components

> Google Cloud CLI 컴포넌트 관리.
> 관련 항목: `gcloud`.
> 더 많은 정보: <https://docs.cloud.google.com/sdk/gcloud/reference/components>.

- 설치 가능한 컴포넌트 목록 표시:

`gcloud components list`

- 하나 이상의 컴포넌트 설치 (의존성도 함께 설치됨):

`gcloud components install {{컴포넌트_아이디1 컴포넌트_아이디2 ...}}`

- 모든 컴포넌트를 최신 버전으로 업데이트:

`gcloud components update`

- 모든 컴포넌트를 특정 버전으로 업데이트:

`gcloud components update --version={{1.2.3}}`

- 확인 과정 없이 컴포넌트 업데이트 (자동화 스크립트에 유용):

`gcloud components update --quiet`
