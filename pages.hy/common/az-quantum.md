#ազ քվանտ

> Կառավարեք Azure Quantum աշխատանքային տարածքները և ներկայացրեք քվանտային աշխատանքները մատակարարներին (նախադիտում, պահանջում է քվանտային ընդլայնում):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/quantum>:.

- Ստեղծեք նոր Azure Quantum աշխատանքային տարածք.:

`az quantum workspace create {{[-g|--resource-group]}} {{ResourceGroup}} {{[-l|--location]}} {{Location}} {{[-w|--workspace-name]}} {{Workspace}} {{[-a|--storage-account]}} {{MyStorageAccountName}}`

- Թվարկեք բոլոր Azure Quantum աշխատանքային տարածքները.:

`az quantum workspace list`

- Սահմանեք լռելյայն Azure Quantum աշխատանքային տարածք.:

`az quantum workspace set {{[-g|--resource-group]}} {{ResourceGroup}} {{[-w|--workspace-name]}} {{Workspace}}`

- Ներկայացրեք QIR քվանտային աշխատանք թիրախին.:

`az quantum job submit {{[-g|--resource-group]}} {{ResourceGroup}} {{[-w|--workspace-name]}} {{Workspace}} {{[-l|--location]}} {{Location}} {{[-t|--target-id]}} {{Id}} --job-name {{Job}} --job-input-file {{QirBitcode.bc}} --job-input-format {{qir.v1}}`

- Թվարկեք բոլոր աշխատանքները Quantum Workspace-ում.:

`az quantum job list {{[-g|--resource-group]}} {{ResourceGroup}} {{[-l|--location]}} {{Location}} {{[-w|--workspace-name]}} {{Workspace}}`

- Ստացեք քվանտային աշխատանքի արդյունքը.:

`az quantum job output {{[-g|--resource-group]}} {{ResourceGroup}} {{[-w|--workspace-name]}} {{Workspace}} --job-id {{Job}}`

- Ցուցակեք հասանելի մատակարարների առաջարկները մի վայրում.:

`az quantum offerings list {{[-l|--location]}} {{Location}}`

- Սահմանեք լռելյայն թիրախ աշխատանքի ներկայացման համար.:

`az quantum target set {{[-t|--target-id]}} {{Id}}`
