# aws acm-pca

> AWS 인증서 관리자 개인 인증 기관.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html>.

- 개인 인증 기관 생성:

`aws acm-pca create-certificate-authority --certificate-authority-configuration {{ca_config}} --idempotency-token {{token}} --permanent-deletion-time-in-days {{number}}`

- 개인 인증 기관 정보 표시:

`aws acm-pca describe-certificate-authority --certificate-authority-arn {{ca_arn}}`

- 개인 인증 기관 목록:

`aws acm-pca list-certificate-authorities`

- 인증 기관 업데이트:

`aws acm-pca update-certificate-authority --certificate-authority-arn {{ca_arn}} --certificate-authority-configuration {{ca_config}} --status {{status}}`

- 개인 인증 기관 삭제:

`aws acm-pca delete-certificate-authority --certificate-authority-arn {{ca_arn}}`

- 인증서 발행:

`aws acm-pca issue-certificate --certificate-authority-arn {{ca_arn}} --certificate-signing-request {{cert_signing_request}} --signing-algorithm {{algorithm}} --validity {{validity}}`

- 인증서 취소:

`aws acm-pca revoke-certificate --certificate-authority-arn {{ca_arn}} --certificate-serial {{serial}} --reason {{reason}}`

- 인증서 세부사항 출력:

`aws acm-pca get-certificate --certificate-authority-arn {{ca_arn}} --certificate-arn {{cert_arn}}`
