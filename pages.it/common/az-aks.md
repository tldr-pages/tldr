# az aks

> Gestisce i cluster Azure Kubernetes Service (AKS).
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/aks>.

- Elenca i cluster AKS:

`az aks list {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Crea un nuovo cluster AKS:

`az aks create {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome}} {{[-c|--node-count]}} {{conteggio}} --node-vm-size {{dimensione}}`

- Elimina un cluster AKS:

`az aks delete {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome}}`

- Ottiene le credenziali di accesso per un cluster AKS:

`az aks get-credentials {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome}}`

- Ottiene le versioni di upgrade disponibili per un cluster AKS:

`az aks get-upgrades {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome}}`
