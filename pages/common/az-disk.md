# az disk

> Manage Azure Managed Disks.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/disk>.

- Create a managed disk:

`az disk create --resource-group {{resource_group}} --name {{disk_name}} --size-gb {{size_in_gb}}`

- List managed disks in a resource group:

`az disk list --resource-group {{resource_group}}`

- Delete a managed disk:

`az disk delete --resource-group {{resource_group}} --name {{disk_name}}`

- Grant read or write access to a managed disk (for export):

`az disk grant-access --resource-group {{resource_group}} --name {{disk_name}} --access-level {{Read|Write}} --duration-in-seconds {{seconds}}`

- Update disk size:

`az disk update --resource-group {{resource_group}} --name {{disk_name}} --size-gb {{new_size_in_gb}}`
