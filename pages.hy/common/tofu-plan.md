# tofu պլան

> Ստեղծեք և ցուցադրեք OpenTofu-ի կատարման պլանները:.
> Լրացուցիչ տեղեկություններ. <https://opentofu.org/docs/cli/commands/plan/>:.

- Ստեղծեք և ցուցադրեք կատարման պլանը ընթացիկ գրացուցակում.:

`tofu plan`

- Ցույց տալ ծրագիր՝ ոչնչացնելու բոլոր հեռավոր օբյեկտները, որոնք ներկայումս գոյություն ունեն.:

`tofu plan -destroy`

- Ցույց տվեք Tofu վիճակի և ելքային արժեքների թարմացման ծրագիր.:

`tofu plan -refresh-only`

- Նշեք արժեքներ մուտքագրման փոփոխականների համար.:

`tofu plan -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Կենտրոնացեք Tofu-ի ուշադրությունը ռեսուրսների միայն մի ենթախմբի վրա.:

`tofu plan -target {{resource_type.resource_name[instance index]}}`

- Արտադրեք պլան որպես JSON.:

`tofu plan -json`

- Գրեք պլան կոնկրետ ֆայլում.:

`tofu plan -no-color > {{path/to/file}}`
