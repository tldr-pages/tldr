# ավս

> Պաշտոնական CLI գործիքը Amazon վեբ ծառայությունների համար:.
> Որոշ ենթահրամաններ, ինչպիսիք են `s3`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/>:.

- Կարգավորեք AWS հրամանի տողը.:

`aws configure wizard`

- Կարգավորեք AWS հրամանի տողը SSO-ի միջոցով.:

`aws configure sso`

- Ստացեք զանգահարողի ինքնությունը (օգտագործվում է թույլտվությունները շտկելու համար).:

`aws sts get-caller-identity`

- Թվարկեք AWS ռեսուրսները տարածաշրջանում և թողարկեք YAML-ում.:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Օգտագործեք ավտոմատ հուշում հրամանի հարցում օգնելու համար.:

`aws iam create-user --cli-auto-prompt`

- Ստացեք ինտերակտիվ հրաշագործ AWS ռեսուրսի համար.:

`aws dynamodb wizard {{new_table}}`

- Ստեղծեք JSON CLI Skeleton (օգտակար ենթակառուցվածքի համար որպես կոդ).:

`aws dynamodb update-table --generate-cli-skeleton`

- Ցուցադրել օգնություն կոնկրետ հրամանի համար.:

`aws {{command}} help`
