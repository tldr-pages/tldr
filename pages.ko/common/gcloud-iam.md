# gcloud iam

> Identity and Access Management (IAM) 환경 설정 및 서비스 계정을 구성합니다.
> 같이 보기: `gcloud`.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/iam>.

- 리소스에 대한 IAM 부여 가능한 역할 나열:

`gcloud iam list-grantable-roles {{리소스}}`

- 조직 또는 프로젝트에 대한 사용자 정의 역할 생성:

`gcloud iam roles create {{역할_이름}} --{{조직|프로젝트}} {{조직|프로젝트_아이디}} --file {{경로/대상/role.yaml}}`

- 프로젝트에 대한 서비스 계정 생성:

`gcloud iam service-accounts create {{이름}}`

- 서비스 계정에 IAM 정책 바인딩 추가:

`gcloud iam service-accounts add-iam-policy-binding {{서비스_계정_이메일}} --member {{멤버}} --role {{역할}}`

- 기존 IAM 정책 바인딩 교체:

`gcloud iam service-accounts set-iam-policy {{서비스_계정_이메일}} {{정책_파일}}`

- 서비스 계정의 키 나열:

`gcloud iam service-accounts keys list --iam-account {{서비스_계정_이메일}}`
