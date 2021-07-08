# az account

> Manage Azure subscription information.
> More information: <https://docs.microsoft.com/cli/azure/account>.

- Print a list of subscriptions for the logged in account:

`az account list`

- Set a `subscription` to be the current active subscription:

`az account set --subscription {{subscription_id}}`

- List supported regions for the currently active subscription:

`az account list-locations`

- Print an access token to be used with `MS Graph API`:

`az account get-access-token --resource-type {{ms-graph}}`

- Print details of the current active subscription in specified format:

`az account show --output {{json|tsv|table|yaml}}`
