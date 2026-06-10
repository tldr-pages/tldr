# prowler aws

> Գնահատեք AWS անվտանգության լավագույն փորձը, կատարեք աուդիտ, համապատասխանության ստուգումներ և ստեղծեք հաշվետվություններ:.
> Տես նաև՝ `prowler`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`:.
> Լրացուցիչ տեղեկություններ. <https://docs.prowler.com/user-guide/cli/tutorials/misc>:.

- AWS հաշվի վրա գործարկեք կանխադրված ստուգումների շարքը.:

`prowler aws`

- Օգտագործեք հատուկ AWS պրոֆիլ և զտեք աուդիտի ենթարկված շրջանները.:

`prowler aws {{[-p|--profile]}} {{custom-profile}} {{[-f|--filter-region]}} {{us-east-1 eu-south-2 ...}}`

- Գործարկեք ստուգումներ ընտրված AWS ծառայությունների համար.:

`prowler aws {{[-s|--services]}} {{s3|ec2|...}}`

- Գործարկեք հատուկ AWS ստուգում.:

`prowler aws {{[-c|--checks]}} {{s3_bucket_public_access}}`

- Բացառել հատուկ ստուգումներ կամ ծառայություններ.:

`prowler aws {{[-e|--excluded-checks]}} {{s3_bucket_public_access}} --exclude-services {{s3|ec2|...}}`
