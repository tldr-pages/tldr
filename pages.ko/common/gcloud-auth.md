# gcloud auth

> `gcloud`에 대한 권한 부여 및 취소, 자격 증명 관리.
> 같이 보기: `gcloud`.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/auth>.

- Google Cloud 사용자 자격 증명으로 `gcloud` CLI에 대한 액세스를 허용하고 현재 계정을 활성 계정으로 설정:

`gcloud auth login`

- 서비스 계정 자격 증명으로 `gcloud auth login`과 유사하게 Google Cloud 액세스 허용:

`gcloud auth activate-service-account`

- Cloud Client Libraries를 위한 애플리케이션 기본 자격 증명(ADC) 관리:

`gcloud auth application-default`

- 시스템에서 현재 인증된 Google Cloud 계정 목록 표시:

`gcloud auth list`

- 현재 계정의 액세스 토큰 표시:

`gcloud auth print-access-token`

- 계정의 액세스 자격 증명 제거:

`gcloud auth revoke`
