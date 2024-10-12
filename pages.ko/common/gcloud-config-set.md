# gcloud config set

> Google Cloud CLI 구성에서 속성을 설정.
> 속성은 Google Cloud CLI 동작의 다양한 측면을 제어합니다.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/config/set>.

- core 섹션에서 프로젝트 속성 설정:

`gcloud config set project {{프로젝트_ID}}`

- 향후 작업을 위한 컴퓨트 영역 설정:

`gcloud config set compute/zone {{존_이름}}`

- 스크립팅에 적합하도록 gcloud의 프롬프트 비활성화:

`gcloud config set disable_prompts true`

- 현재 사용 중인 속성 목록 보기:

`gcloud config list`

- 설정된 속성 해제:

`gcloud config unset {{속성_이름}}`

- 새로운 구성 프로필 생성:

`gcloud config configurations create {{구성_이름}}`

- 다른 구성 프로필 간 전환:

`gcloud config configurations activate {{구성_이름}}`
