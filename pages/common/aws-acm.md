# aws acm

> AWS Certificate Manager.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

- Import a certificate:

`aws acm import-certificate --certificate-arn {{certificate_arn}} --certificate {{certificate}} --private-key {{private_key}} --certificate-chain {{certificate_chain}}`

- List certificates:

`aws acm list-certificates`

- Describe a certificate:

`aws acm describe-certificate --certificate-arn {{certificate_arn}}`

- Request a certificate:

`aws acm request-certificate --domain-name {{domain_name}} --validation-method {{validation_method}}`

- Delete a certificate:

`aws acm delete-certificate --certificate-arn {{certificate_arn}}`

- List certificate validations:

`aws acm list-certificates --certificate-statuses {{status}}`

- Get certificate details:

`aws acm get-certificate --certificate-arn {{certificate_arn}}`

- Update certificate options:

`aws acm update-certificate-options --certificate-arn {{certificate_arn}} --options {{options}}`
