# ազ ցանց

> Կառավարեք Azure ցանցի ռեսուրսները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/network>:.

- Թվարկե՛ք տարածաշրջանի ցանցային ռեսուրսները, որոնք օգտագործվում են բաժանորդագրության քվոտայի դիմաց.:

`az network list-usages`

- Թվարկեք բոլոր վիրտուալ ցանցերը բաժանորդագրության մեջ.:

`az network vnet list`

- Ստեղծեք վիրտուալ ցանց.:

`az network vnet create --address-prefixes {{10.0.0.0/16}} {{[-n|--name]}} {{vnet}} {{[-g|--resource-group]}} {{group_name}} --subnet-name {{subnet}} --subnet-prefixes {{10.0.0.0/24}}`

- Միացնել արագացված ցանցը ցանցային ինտերֆեյսի քարտի համար.:

`az network nic update --accelerated-networking true {{[-n|--name]}} {{nic}} {{[-g|--resource-group]}} {{resource_group}}`
