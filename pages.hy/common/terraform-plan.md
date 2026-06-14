# երկրային պլան

> Ստեղծեք և ցուցադրեք Terraform-ի կատարման պլանները:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/terraform/cli/commands/plan>:.

- Ստեղծեք և ցուցադրեք կատարման պլանը ընթացիկ գրացուցակում.:

`terraform plan`

- Ցույց տալ ծրագիր՝ ոչնչացնելու բոլոր հեռավոր օբյեկտները, որոնք ներկայումս գոյություն ունեն.:

`terraform plan -destroy`

- Ցույց տվեք Terraform վիճակի և ելքային արժեքների թարմացման ծրագիր.:

`terraform plan -refresh-only`

- Նշեք արժեքներ մուտքագրման փոփոխականների համար.:

`terraform plan -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Terraform-ի ուշադրությունը կենտրոնացրեք ռեսուրսների միայն ենթաբազմության վրա.:

`terraform plan -target {{resource_type.resource_name[instance_index]}}`

- Արտադրեք պլան որպես JSON.:

`terraform plan -json`

- Գրեք պլան կոնկրետ ֆայլում.:

`terraform plan -no-color > {{path/to/file}}`
