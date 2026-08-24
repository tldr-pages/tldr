# az vm

> Gestisce le macchine virtuali in Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/vm>.

- Visualizza una tabella delle Virtual Machines disponibili:

`az vm list --output table`

- Crea una macchina virtuale usando l'immagine Ubuntu predefinita e genera chiavi SSH:

`az vm create {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nome_vm}} --image {{UbuntuLTS}} --admin-user {{azureuser}} --generate-ssh-keys`

- Ferma una Virtual Machine:

`az vm stop {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nome_vm}}`

- Dealloca una Virtual Machine:

`az vm deallocate {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nome_vm}}`

- Avvia una Virtual Machine:

`az vm start {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nome_vm}}`

- Riavvia una Virtual Machine:

`az vm restart {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nome_vm}}`

- Elenca le immagini VM disponibili nel marketplace Azure:

`az vm image list`
