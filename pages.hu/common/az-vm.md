# az vm

> Virtuális gépek kezelése az Azure-ban. A `azure-cli` weboldal része. További információ: <https://learn.microsoft.com/cli/azure/vm>.

- Az elérhető virtuális gépek adatainak listája:

`az vm list`

- Hozzon létre egy virtuális gépet az alapértelmezett Ubuntu kép használatával, és generáljon ssh-kulcsokat:

`az vm create --resource-group {{rg}} --name {{vm_name}} --image {{UbuntuLTS}} --admin-user {{azureuser}} --generate-ssh-keys`

- Virtuális gép leállítása:

`az vm stop --resource-group {{rg}} --name {{vm_name}}`

- Virtuális gép kiosztásának megszüntetése:

`az vm deallocate --resource-group {{rg}} --name {{vm_name}}`

- Virtuális gép indítása:

`az vm start --resource-group {{rg}} --name {{vm_name}}`

- Virtuális gép újraindítása:

`az vm restart --resource-group {{rg}} --name {{vm_name}}`

- Az Azure Marketplace-en elérhető VM-képek listázása:

`az vm image list`
