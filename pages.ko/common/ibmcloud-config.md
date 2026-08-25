# ibmcloud config

> IBM Cloud CLI 설정 값 수정 또는 조회.
> 더 많은 정보: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_config>.

- HTTP 요청 타임아웃을 30초로 설정:

`ibmcloud config --http-timeout 30`

- HTTP 요청의 trace 출력 활성화:

`ibmcloud config --trace true`

- HTTP 요청 trace를 특정 파일에 기록:

`ibmcloud config --trace {{경로/대상/trace_파일}}`

- 색상 출력 비활성화:

`ibmcloud config --color false`

- 로케일을 특정 언어로 설정:

`ibmcloud config --locale {{zh_Hans}}`

- SSO 일회용 패스코드 자동 승인 활성화:

`ibmcloud config --sso-otp auto`
