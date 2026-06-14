# ազ խորհրդական

> Կառավարեք Azure-ի բաժանորդագրության տեղեկատվությունը:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/advisor>:.

- Ցուցակեք Azure Advisor-ի կազմաձևումը ամբողջ բաժանորդագրության համար.:

`az advisor configuration list`

- Ցույց տալ Azure Advisor-ի կոնֆիգուրացիան տվյալ բաժանորդագրության կամ ռեսուրսների խմբի համար.:

`az advisor configuration show {{[-g|--resource-group]}} {{resource_group}}`

- Թվարկեք Azure Advisor-ի առաջարկությունները.:

`az advisor recommendation list`

- Միացնել Azure Advisor-ի առաջարկությունները.:

`az advisor recommendation enable {{[-g|--resource-group]}} {{resource_group}}`

- Անջատեք Azure Advisor-ի առաջարկությունները.:

`az advisor recommendation disable {{[-g|--resource-group]}} {{resource_group}}`
