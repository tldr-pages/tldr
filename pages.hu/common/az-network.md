# az network

> Azure hálózati erőforrások kezelése. A `azure-cli` webhely része. További információ: <https://learn.microsoft.com/cli/azure/network>.

- Az előfizetési kvótával szemben használt hálózati erőforrások listázása egy régióban:

`az network list-usages`

- Az összes virtuális hálózat listázása egy előfizetésben:

`az network vnet list`

- Virtuális hálózat létrehozása:

`az network vnet create --address-prefixes {{10.0.0.0/16}} --name {{vnet}} --resource_group {{group_name}} --submet-name {{subnet}} --subnet-prefixes {{10.0.0.0/24}}`

- Gyorsított hálózat engedélyezése egy hálózati illesztőkártya számára:

`az network nic update --accelerated-networking true --name {{nic}} --resource-group {{resource_group}}`
