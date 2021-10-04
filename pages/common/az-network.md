# az network

> Manage Azure Network resources.
> Part of `azure-cli`.
> More information: <https://docs.microsoft.com/cli/azure/network>.

- List network resources in a region that are used against a subscription quota:

`az network list-usages`

- List all virtual networks in a subscription:

`az network vnet list`

- Create a virtual network:

`az network vnet create --address-prefixes {{10.0.0.0/16}} --name {{my_vnet}} --resource_group {{group_name}} --submet-name {{my_subnet}} --subnet-prefixes {{10.0.0.0/24}}`

- Enable accelerated networking for a network interface card:

`az network nic update --accelerated-networking true --name {{my_nic}} --resource-group {{resource_group}}`
