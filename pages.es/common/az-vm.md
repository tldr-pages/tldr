# az vm

> Administra máquinas virtuales en Azure.
> Parte de `azure-cli`.
> Más información: <https://learn.microsoft.com/cli/azure/vm>.

- Lista los detalles de las máquinas virtuales disponibles:

`az vm list`

- Crea una máquina virtual `UbuntuServer 18.04 LTS` y genera claves ssh:

`az vm create --resource-group {{grupo_de_recursos}} --name {{nombre}} --image {{Canonical:UbuntuServer:18.04-LTS:latest}} --admin-user {{usuario_azure}} --generate-ssh-keys`

- Detiene una máquina virtual:

`az vm stop --resource-group {{grupo_de_recursos}} --name {{nombre}}`

- Desasigna una máquina virtual:

`az vm deallocate --resource-group {{grupo_de_recursos}} --name {{nombre}}`

- Inicia una máquina virtual:

`az vm start --resource-group {{grupo_de_recursos}} --name {{nombre}}`

- Reinicia una máquina virtual:

`az vm restart --resource-group {{grupo_de_recursos}} --name {{nombre}}`

- Lista las imágenes de VM disponibles en el Azure Marketplace:

`az vm image list`
