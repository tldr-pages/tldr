# prowler azure

> Azure의 보안 모범 사례 점검, 보안 감사, 규정 준수 검사 및 보고서 생성을 수행.
> 관련 항목: `prowler`, `prowler-aws`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`.
> 더 많은 정보: <https://docs.prowler.com/user-guide/cli/tutorials/misc>.

- Azure CLI 인증을 사용하여 현재 Azure 계정에 대해 기본 보안 검사 실행:

`prowler azure --az-cli-auth`

- 지정한 Azure 구독에 대해 보안 검사 실행:

`prowler azure --az-cli-auth --subscription-ids {{구독_아이디1 구독_아이디2 ...}}`

- 환경 변수를 사용한 서비스 주체 인증으로 실행:

`prowler azure --sp-env-auth`

- 브라우저 인증을 사용하고 테넌트 ID를 지정하여 실행:

`prowler azure --browser-auth --tenant-id "{{XXXXXXXX}}"`

- 관리형 ID를 사용해 인증 (예: Azure VM):

`prowler azure --managed-identity-auth`

- 지정한 Azure 서비스에 대해서만 보안 검사 실행:

`prowler azure {{[-s|--services]}} {{defender|iam|...}}`

- 지정한 Azure 보안 감사 실행:

`prowler azure {{[-c|--checks]}} {{스토리지_blob_공개_접근_수준_비활성화됨}}`

- 지정한 보안 검사 또는 서비스를 제외하고 실행:

`prowler azure {{[-e|--excluded-checks]}} {{스토리지_blob_공개_접근_수준_비활성화됨}} --exclude-services {{defender|iam|...}}`
