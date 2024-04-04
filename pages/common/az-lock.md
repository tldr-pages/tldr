# az lock

> Manage Azure locks.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/lock>.

- Create a read-only subscription level lock:

`az lock create --name {{lock_name}} --lock-type ReadOnly`

- Create a read-only resource group level lock:

`az lock create --name {{lock_name}} --resource-group {{group_name}} --lock-type ReadOnly`

- Delete a subscription level lock:

`az lock delete --name {{lock_name}}`

- Delete a resource group level lock:

`az lock delete --name {{lock_name}} --resource-group {{group_name}}`

- List out all locks on the subscription level:

`az lock list`

- Show a subscription level lock with a specific [n]ame:

`az lock show -n {{lock_name}}`
