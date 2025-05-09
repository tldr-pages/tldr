# az vm

> Manage virtual machines in Azure.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/vm>.

- Display a table of available Virtual Machines:

`az vm list --output table`

- Create a virtual machine using the default Ubuntu image and generate SSH keys:

`az vm create {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}} --image {{UbuntuLTS}} --admin-user {{azureuser}} --generate-ssh-keys`

- Stop a Virtual Machine:

`az vm stop {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- Deallocate a Virtual Machine:

`az vm deallocate {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- Start a Virtual Machine:

`az vm start {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- Restart a Virtual Machine:

`az vm restart {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- List VM images available in the Azure Marketplace:

`az vm image list`
