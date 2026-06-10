# aws accm

> AWS վկայագրի կառավարիչ:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/acm/>:.

- Ներմուծեք վկայագիր.:

`aws acm import-certificate --certificate-arn {{certificate_arn}} --certificate {{certificate}} --private-key {{private_key}} --certificate-chain {{certificate_chain}}`

- Ցուցակ վկայականներ.:

`aws acm list-certificates`

- Նկարագրեք վկայականը.:

`aws acm describe-certificate --certificate-arn {{certificate_arn}}`

- Պահանջել վկայական.:

`aws acm request-certificate --domain-name {{domain_name}} --validation-method {{validation_method}}`

- Ջնջել վկայականը.:

`aws acm delete-certificate --certificate-arn {{certificate_arn}}`

- Ցանկ վկայականի վավերացումները.:

`aws acm list-certificates --certificate-statuses {{status}}`

- Ստացեք վկայագրի մանրամասները.:

`aws acm get-certificate --certificate-arn {{certificate_arn}}`

- Թարմացրեք վկայագրի ընտրանքները.:

`aws acm update-certificate-options --certificate-arn {{certificate_arn}} --options {{options}}`
