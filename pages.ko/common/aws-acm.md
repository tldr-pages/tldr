# aws acm

> AWS 인증서 관리자.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

- 인증서 가져오기:

`aws acm import-certificate --certificate-arn {{certificate_arn}} --certificate {{인증서}} --private-key {{개인_키}} --certificate-chain {{인증서_체인}}`

- 인증서 나열:

`aws acm list-certificates`

- 인증서 설명 확인:

`aws acm describe-certificate --certificate-arn {{certificate_arn}}`

- 인증서 요청:

`aws acm request-certificate --domain-name {{도메인_이름}} --validation-method {{검증_방법}}`

- 인증서 삭제:

`aws acm delete-certificate --certificate-arn {{certificate_arn}}`

- 인증서 검증 방법 나열:

`aws acm list-certificates --certificate-statuses {{status}}`

- 인증서 세부 정보 출력:

`aws acm get-certificate --certificate-arn {{certificate_arn}}`

- 인증서 옵션 업데이트:

`aws acm update-certificate-options --certificate-arn {{certificate_arn}} --options {{옵션}}`
