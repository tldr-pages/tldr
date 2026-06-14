# aws acm-pca

> AWS սերտիֆիկատների մենեջեր Մասնավոր սերտիֆիկատների մարմին:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/acm-pca/>:.

- Ստեղծեք մասնավոր սերտիֆիկատի մարմին.:

`aws acm-pca create-certificate-authority --certificate-authority-configuration {{ca_config}} --idempotency-token {{token}} --permanent-deletion-time-in-days {{number}}`

- Նկարագրեք մասնավոր սերտիֆիկատի մարմնին.:

`aws acm-pca describe-certificate-authority --certificate-authority-arn {{ca_arn}}`

- Թվարկեք մասնավոր սերտիֆիկատների մարմինները.:

`aws acm-pca list-certificate-authorities`

- Թարմացրեք սերտիֆիկատի մարմինը.:

`aws acm-pca update-certificate-authority --certificate-authority-arn {{ca_arn}} --certificate-authority-configuration {{ca_config}} --status {{status}}`

- Ջնջել մասնավոր սերտիֆիկատի լիազորությունը.:

`aws acm-pca delete-certificate-authority --certificate-authority-arn {{ca_arn}}`

- Վկայական տրամադրել.:

`aws acm-pca issue-certificate --certificate-authority-arn {{ca_arn}} --certificate-signing-request {{cert_signing_request}} --signing-algorithm {{algorithm}} --validity {{validity}}`

- Չեղյալ համարել վկայականը.:

`aws acm-pca revoke-certificate --certificate-authority-arn {{ca_arn}} --certificate-serial {{serial}} --reason {{reason}}`

- Ստացեք վկայագրի մանրամասները.:

`aws acm-pca get-certificate --certificate-authority-arn {{ca_arn}} --certificate-arn {{cert_arn}}`
