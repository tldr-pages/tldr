# az vm

> Gestiona máquinas virtuales en Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/vm>.

- Muestra una tabla de Máquinas Virtuales disponibles:

`az vm list --output table`

- Crea una máquina virtual usando la imagen por defecto de Ubuntu y genera las claves SSH:

`az vm create {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nombre_vm}} --image {{UbuntuLTS}} --admin-user {{usuarioazure}} --generate-ssh-keys`

- Detiene una Máquina Virtual:

`az vm stop {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nombre_de_la_máquina_virtual}}`

- Desasigna una máquina virtual:

`az vm deallocate {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nombre_de_la_máquina virtual}}`

- Inicia una Máquina Virtual:

`az vm start {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nombre_de_la_máquina_virtual}}`

- Reinicia una Máquina Virtual:

`az vm restart {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{nombre_de_la_máquina_virtual}}`

- Lista de imágenes de máquinas virtuales disponibles en Azure Marketplace:

`az vm image list`
