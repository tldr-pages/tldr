# az vm

> Gestionați mașinile virtuale în Azure.
> O parte din `az`, clientul de linie de comandă pentru Microsoft Azure.
> Mai multe informaţii: <https://docs.microsoft.com/cli/azure/vm>

- Lista detaliilor mașinilor virtuale disponibile:

`az vm list`

- Creați o mașină virtuală `UbuntUserver 18.04 LTS` și generați chei ssh:

`az vm create --resource-group {{rg}} --name {{vm_name}} --image {{Canonical:UbuntuServer:18.04-LTS:latest}} --admin-user {{azureuser}} --generate-ssh-keys`

- Opriți o mașină virtuală:

`az vm stop --resource-group {{rg}} --name {{vm_name}}`

- Deallocați o mașină virtuală:

`az vm deallocate --resource-group {{rg}} --name {{vm_name}}`

- Porniți o mașină virtuală:

`az vm start --resource-group {{rg}} --name {{vm_name}}`

- Reporniți o mașină virtuală:

`az vm restart --resource-group {{rg}} --name {{vm_name}}`

- Lista imaginilor VM disponibile în Azure Marketplace:

`az vm image list`
