# gcloud ես

> Կազմաձևեք նույնականացման և մուտքի կառավարման (IAM) նախապատվությունները և սպասարկման հաշիվները:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/iam>:.

- Նշեք IAM-ի շնորհվող դերերը ռեսուրսի համար.:

`gcloud iam list-grantable-roles {{resource}}`

- Ստեղծեք հատուկ դեր կազմակերպության կամ նախագծի համար.:

`gcloud iam roles create {{role_name}} --{{organization|project}} {{organization|project_id}} --file {{path/to/role.yaml}}`

- Ստեղծեք ծառայության հաշիվ նախագծի համար.:

`gcloud iam service-accounts create {{name}}`

- Ավելացրեք IAM քաղաքականություն, որը պարտադիր է ծառայության հաշվին.:

`gcloud iam service-accounts add-iam-policy-binding {{service_account_email}} --member {{member}} --role {{role}}`

- Փոխարինել գործող IAM քաղաքականությունը պարտադիր.:

`gcloud iam service-accounts set-iam-policy {{service_account_email}} {{policy_file}}`

- Նշեք ծառայության հաշվի բանալիները.:

`gcloud iam service-accounts keys list --iam-account {{service_account_email}}`
