# ազ ակս

> Կառավարեք Azure Kubernetes ծառայության (AKS) կլաստերները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/aks>:.

- Ցուցակեք AKS կլաստերները.:

`az aks list {{[-g|--resource-group]}} {{resource_group}}`

- Ստեղծեք նոր AKS կլաստեր.:

`az aks create {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}} {{[-c|--node-count]}} {{count}} --node-vm-size {{size}}`

- Ջնջել AKS կլաստերը.:

`az aks delete {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}}`

- Ստացեք մուտքի հավատարմագրերը AKS կլաստերի համար.:

`az aks get-credentials {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}}`

- Ստացեք թարմացման տարբերակները, որոնք հասանելի են AKS կլաստերի համար.:

`az aks get-upgrades {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}}`
