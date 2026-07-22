# prowler gcp

> Google Cloud Platform (GCP)의 보안 모범 사례 점검, 보안 감사 및 규정 준수 검사를 수행.
> 관련 항목: `prowler`, `prowler-aws`, `prowler-azure`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`.
> 더 많은 정보: <https://docs.prowler.com/user-guide/cli/tutorials/misc>.

- 기본 사용자 자격 증명을 사용하여, 접근 가능한 모든 GCP 프로젝트에 대해 기본 보안 검사 실행:

`prowler gcp`

- 서비스 계정 자격 증명 파일을 사용하여 인증:

`prowler gcp --credentials-file {{경로/대상/증명_파일.json}}`

- 지정한 GCP 프로젝트 ID에 대해 보안 검사 실행:

`prowler gcp --project-ids {{프로젝트_아이디1 프로젝트_아이디2 ...}}`

- 지정한 GCP 서비스에 대해서만 보안 검사 실행:

`prowler gcp {{[-s|--services]}} {{iam|compute|...}}`

- 지정한 GCP 보안 검사 실행:

`prowler gcp {{[-c|--checks]}} {{gcp_스토리지_버킷_로깅_활성화}}`

- 지정한 보안 검사 또는 서비스를 제외하고 실행:

`prowler gcp {{[-e|--excluded-checks]}} {{gcp_스토리지_버킷_로깅_활성화}} --exclude-services {{iam|compute|...}}`
