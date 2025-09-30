# gcpdiag

> Google Cloud Platform 문제 해결 및 진단 도구.
> Docker 컨테이너 또는 GCP Cloudshell에서 실행.
> 더 많은 정보: <https://github.com/GoogleCloudPlatform/gcpdiag>.

- 프로젝트에서 `gcpdiag`를 실행하고, 모든 규칙을 반환:

`gcpdiag lint --project={{gcp_프로젝트_아이디}}`

- 괜찮은 규칙 숨기기:

`gcpdiag lint --project={{gcp_프로젝트_아이디}} --hide-ok`

- 서비스 계정 비공개 키 파일을 사용해 인증:

`gcpdiag lint --project={{gcp_프로젝트_아이디}} --auth-key {{경로/대상/개인_키}}`

- 며칠 전의 로그 및 지표를 검색 (기본값: 3일):

`gcpdiag lint --project={{gcp_프로젝트_아이디}} --within-days {{숫자}}`

- 도움말 표시:

`gcpdiag lint --help`
