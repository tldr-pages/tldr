#էոլ

> Ցույց տալ կյանքի ավարտի ժամկետները (EoLs) մի շարք ապրանքների համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/hugovk/norwegianblue#example-command-line-use>:.

- Նշեք բոլոր հասանելի ապրանքները.:

`eol`

- Ստացեք մեկ կամ մի քանի ապրանքների EoL-ներ.:

`eol {{product1 product2 ...}}`

- Բացեք արտադրանքի վեբ էջը.:

`eol {{product}} {{[-w|--web]}}`

- Ստացեք մեկ կամ մի քանի արտադրանքի EoL-ներ հատուկ ձևաչափով.:

`eol {{product1 product2 ...}} --{{html|json|md|markdown|pretty|rst|csv|tsv|yaml}}`

- Ստացեք մեկ կամ մի քանի արտադրանքի EoL-ներ որպես մեկ նշագրման ֆայլ.:

`eol {{product1 product2 ...}} --{{markdown}} > {{eol_report.md}}`

- Ցուցադրել օգնությունը.:

`eol {{[-h|--help]}}`
