# gcpdiag

> Google Cloud Platform-ի անսարքությունների վերացման և ախտորոշման գործիք:.
> Գործարկեք Docker կոնտեյներով կամ GCP Cloudshell-ում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/GoogleCloudPlatform/gcpdiag#usage>:.

- Գործարկեք `gcpdiag`-ը ձեր նախագծի վրա՝ վերադարձնելով բոլոր կանոնները.:

`gcpdiag lint --project {{gcp_project_id}}`

- Թաքցնել կանոնները, որոնք լավ են.:

`gcpdiag lint --project {{gcp_project_id}} --hide-ok`

- Նույնականացրեք՝ օգտագործելով ծառայության հաշվի մասնավոր բանալի ֆայլը.:

`gcpdiag lint --project {{gcp_project_id}} --auth-key {{path/to/private_key}}`

- Որոնեք տեղեկամատյանները և չափումները մի քանի օրից (կանխադրված՝ 3 օր).:

`gcpdiag lint --project {{gcp_project_id}} --within-days {{number}}`

- Ցուցադրել օգնությունը.:

`gcpdiag lint --help`
