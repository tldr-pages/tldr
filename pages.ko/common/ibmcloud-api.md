# ibmcloud api

> IBM Cloud API 엔드포인트 설정 또는 조회.
> 더 많은 정보: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_api>.

- 현재 API 엔드포인트 표시:

`ibmcloud api`

- API 엔드포인트를 `cloud.ibm.com`으로 설정:

`ibmcloud api cloud.ibm.com`

- 프라이빗 API 엔드포인트 설정:

`ibmcloud api private.cloud.ibm.com`

- 프라이빗 엔드포인트에 VPC 연결 사용:

`ibmcloud api private.cloud.ibm.com --vpc`

- HTTP 요청의 SSL 검증 우회:

`ibmcloud api https://cloud.ibm.com --skip-ssl-validation`

- API 엔드포인트 설정 제거:

`ibmcloud api --unset`
