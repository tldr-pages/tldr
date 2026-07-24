# prowler

> AWS, Azure, Google Cloud, Kubernetes의 보안 모범 사례 점검, 보안 감사 및 규정 준수 검사를 수행.
> 관련 항목: `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`.
> 더 많은 정보: <https://docs.prowler.com/user-guide/cli/tutorials/misc>.

- AWS, Azure, GCP 또는 Kubernetes 공급자에 대해 기본 보안 검사 실행:

`prowler {{공급자}}`

- 지정한 공급자에서 사용 가능한 모든 검사 목록 표시:

`prowler {{공급자}} {{[-l|--list-checks]}}`

- 지정한 공급자에서 사용 가능한 모든 서비스 목록 표시:

`prowler {{공급자}} --list-services`

- 여러 형식(AWS Security Hub용 JSON-ASFF를 포함)으로 결과 생성:

`prowler {{공급자}} --output-modes {{csv,json-asff,html,...}}`

- 자세한 모드로 실행:

`prowler {{공급자}} --verbose`

- 상태를 기준으로 결과 필터링:

`prowler {{공급자}} --status {{PASS,FAIL,MANUAL}}`

- 도움말 표시:

`prowler --help`

- 버전 정보 표시:

`prowler {{[-v|--version]}}`
