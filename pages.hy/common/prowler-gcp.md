# prowler gcp

> Գնահատեք Google Cloud Platform-ի (GCP) անվտանգության լավագույն փորձը, աուդիտը և համապատասխանության ստուգումները:.
> Տես նաև՝ `prowler`, `prowler-aws`, `prowler-azure`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`:.
> Լրացուցիչ տեղեկություններ. <https://docs.prowler.com/user-guide/cli/tutorials/misc>:.

- Գործարկեք ստուգումների լռելյայն հավաքածուն բոլոր հասանելի GCP նախագծերի վրա՝ օգտագործելով լռելյայն օգտագործողի հավատարմագրերը.:

`prowler gcp`

- Նույնականացրեք ծառայության հաշվի հավատարմագրերի ֆայլի միջոցով.:

`prowler gcp --credentials-file {{path/to/credentials.json}}`

- Սկանավորեք հատուկ GCP նախագծեր ID-ով.:

`prowler gcp --project-ids {{project_id1 project_id2 ...}}`

- Գործարկեք ստուգումներ ընտրված GCP ծառայությունների համար.:

`prowler gcp {{[-s|--services]}} {{iam|compute|...}}`

- Գործարկել հատուկ GCP ստուգում.:

`prowler gcp {{[-c|--checks]}} {{gcp_storage_bucket_logging_enabled}}`

- Բացառել հատուկ ստուգումներ կամ ծառայություններ.:

`prowler gcp {{[-e|--excluded-checks]}} {{gcp_storage_bucket_logging_enabled}} --exclude-services {{iam|compute|...}}`
