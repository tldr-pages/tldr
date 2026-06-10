# պտտվող m365

> Գնահատեք Microsoft 365 (M365) անվտանգության կոնֆիգուրացիաները և լավագույն փորձը:.
> Տես նաև՝ `prowler`, `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-github`:.
> Լրացուցիչ տեղեկություններ. <https://docs.prowler.com/user-guide/cli/tutorials/misc>:.

- Գործարկեք Prowler-ը համակցված ծառայության հիմնական և օգտագործողի հավատարմագրերով.:

`prowler m365 --env-auth`

- Նույնականացրեք՝ օգտագործելով ծառայության սկզբունքը՝:

`prowler m365 --sp-env-auth`

- Նույնականացրեք Azure CLI-ի միջոցով.:

`prowler m365 --az-cli-auth`

- Նույնականացրեք բրաուզերի միջոցով և նշեք վարձակալի ID-ն.:

`prowler m365 --browser-auth --tenant-id "{{XXXXXXXX}}"`

- Գործարկել հատուկ Microsoft 365 ստուգում.:

`prowler m365 {{[-c|--checks]}} {{etcd_enm365_onedrive_sharing_enabledcryption}}`

- Բացառել հատուկ ստուգումները.:

`prowler m365 {{[-e|--excluded-checks]}} {{m365_onedrive_sharing_enabled}}`
