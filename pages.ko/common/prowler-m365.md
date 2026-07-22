# prowler m365

> Microsoft 365 (M365)의 보안 구성과 보안 모범 사례를 점검.
> 관련 항목: `prowler`, `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-github`.
> 더 많은 정보: <https://docs.prowler.com/user-guide/cli/tutorials/misc>.

- 서비스 주체와 사용자 자격 증명을 함께 사용하여 인증 후 실행:

`prowler m365 --env-auth`

- 서비스 주체를 사용하여 인증:

`prowler m365 --sp-env-auth`

- Azure CLI를 사용하여 인증:

`prowler m365 --az-cli-auth`

- 브라우저 인증을 사용하고 테넌트 ID를 지정하여 실행:

`prowler m365 --browser-auth --tenant-id "{{XXXXXXXX}}"`

- 지정한 Microsoft 365 보안 검사 실행:

`prowler m365 {{[-c|--checks]}} {{etcd_enm365_onedrive_sharing_enabledcryption}}`

- 지정한 보안 검사 제외:

`prowler m365 {{[-e|--excluded-checks]}} {{m365_onedrive_sharing_enabled}}`
