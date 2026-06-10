# prowler azure

> Գնահատեք Azure-ի անվտանգության լավագույն փորձը, կատարեք աուդիտ, համապատասխանության ստուգումներ և ստեղծեք հաշվետվություններ:.
> Տես նաև՝ `prowler`, `prowler-aws`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`:.
> Լրացուցիչ տեղեկություններ. <https://docs.prowler.com/user-guide/cli/tutorials/misc>:.

- Գործարկեք ստուգումների լռելյայն հավաքածուն ընթացիկ Azure հաշվի վրա՝ օգտագործելով Azure CLI նույնականացումը.:

`prowler azure --az-cli-auth`

- Գործարկեք ստուգումներ Azure-ի հատուկ բաժանորդագրությունների համար.:

`prowler azure --az-cli-auth --subscription-ids {{subscription_id1 subscription_id2 ...}}`

- Նույնականացրե՛ք՝ օգտագործելով ծառայության սկզբունքը շրջակա միջավայրի փոփոխականների միջոցով.:

`prowler azure --sp-env-auth`

- Նույնականացրեք բրաուզերի մուտքի միջոցով և նշեք վարձակալի ID.:

`prowler azure --browser-auth --tenant-id "{{XXXXXXXX}}"`

- Նույնականացրեք՝ օգտագործելով կառավարվող ինքնությունը (օրինակ՝ Azure VM-ի համար).:

`prowler azure --managed-identity-auth`

- Գործարկեք ստուգումներ ընտրված Azure ծառայությունների համար.:

`prowler azure {{[-s|--services]}} {{defender|iam|...}}`

- Գործարկեք հատուկ Azure ստուգում.:

`prowler azure {{[-c|--checks]}} {{storage_blob_public_access_level_is_disabled}}`

- Բացառել հատուկ ստուգումներ կամ ծառայություններ.:

`prowler azure {{[-e|--excluded-checks]}} {{storage_blob_public_access_level_is_disabled}} --exclude-services {{defender|iam|...}}`
