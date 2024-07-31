# aws acm-pca

> AWS Certificate Manager Private Certificate Authority.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html>.

- Create a private certificate authority:

`aws acm-pca create-certificate-authority --certificate-authority-configuration {{certificate_authority_configuration}} --idempotency-token {{idempotency_token}} --permanent-deletion-time-in-days {{permanent_deletion_time_in_days}}`

- Describe a private certificate authority:

`aws acm-pca describe-certificate-authority --certificate-authority-arn {{certificate_authority_arn}}`

- List private certificate authorities:

`aws acm-pca list-certificate-authorities`

- Update a certificate authority:

`aws acm-pca update-certificate-authority --certificate-authority-arn {{certificate_authority_arn}} --certificate-authority-configuration {{certificate_authority_configuration}} --status {{status}}`

- Delete a private certificate authority:

`aws acm-pca delete-certificate-authority --certificate-authority-arn {{certificate_authority_arn}}`

- Issue a certificate:

`aws acm-pca issue-certificate --certificate-authority-arn {{certificate_authority_arn}} --certificate-signing-request {{certificate_signing_request}} --signing-algorithm {{signing_algorithm}} --validity {{validity}}`

- Revoke a certificate:

`aws acm-pca revoke-certificate --certificate-authority-arn {{certificate_authority_arn}} --certificate-serial {{certificate_serial}} --reason {{reason}}`

- Get certificate details:

`aws acm-pca get-certificate --certificate-authority-arn {{certificate_authority_arn}} --certificate-arn {{certificate_arn}}`
