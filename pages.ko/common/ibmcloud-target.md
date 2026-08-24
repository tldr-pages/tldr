# ibmcloud target

> 대상 계정, 리전 또는 리소스 그룹 설정 및 조회.
> 더 많은 정보: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target>.

- 현재 대상 계정과 리전 정보 표시:

`ibmcloud target`

- 대상 계정 설정:

`ibmcloud target -c {{계정_아이디}}`

- 특정 리전으로 전환:

`ibmcloud target -r {{리전_이름}}`

- 대상 리소스 그룹 설정:

`ibmcloud target -g {{리소스_그룹_이름}}`

- 설정된 리전 해제:

`ibmcloud target --unset-region`

- 설정된 리소스 그룹 해제:

`ibmcloud target --unset-resource-group`
