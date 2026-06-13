# az image

> Manage custom Virtual Machine Images in Azure.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/image>.

- List the custom images under a resource group:

`az image list {{[-g|--resource-group]}} {{resource_group}}`

- Create a custom image from managed disks or snapshots:

`az image create {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}} --os-type {{windows|linux}} --source {{os_disk_source}}`

- Delete a custom image:

`az image delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Show details of a custom image:

`az image show {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Update custom images:

`az image update {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} --set {{property=value}}`
