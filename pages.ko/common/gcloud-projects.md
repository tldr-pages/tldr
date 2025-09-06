# gcloud projects

> Google Cloud에서 프로젝트 액세스 정책 관리.
> 같이 보기: `gcloud`.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/projects>.

- 새 프로젝트 생성:

`gcloud projects create {{프로젝트_아이디|프로젝트_번호}}`

- 모든 활성 프로젝트 나열:

`gcloud projects list`

- 프로젝트의 메타데이터 표시:

`gcloud projects describe {{프로젝트_아이디}}`

- 프로젝트 삭제:

`gcloud projects delete {{프로젝트_아이디|프로젝트_번호}}`

- 지정된 프로젝트에 IAM 정책 바인딩 추가:

`gcloud projects add-iam-policy-binding {{프로젝트_아이디}} --member {{주체}} --role {{역할}}`
