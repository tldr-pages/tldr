# az provider

> Manage resource providers.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/provider>.

- Register a provider:

`az provider register --namespace {{Microsoft.PolicyInsights}}`

- Unregister a provider:

`az provider unregister --namespace {{Microsoft.Automation}}`

- List all providers for a subscription:

`az provider list`

- Show information about a specific provider:

`az provider show --namespace {{Microsoft.Storage}}`

- List all resource types for a specific provider:

`az provider list --query "[?namespace=='{{Microsoft.Network}}'].resourceTypes[].resourceType"`
