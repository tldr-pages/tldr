# az tag

> Manage tags on a resource.
> Part of `azure-cli`.
> More information: <https://docs.microsoft.com/cli/azure/tag>.

- Create a tag value:

`az tag add-value --name {{tag_name}} --value {{tag_value}}`

- Create a tag in the subscription:

`az tag create --name {{tag_name}}`

- Delete a tag from the subscription:

`az tag delete --name {{tag_name}}`

- List all tags on a subscription:

`az tag list --resource-id /subscriptions/{{subscription_id}}`

- Delete a tag value for a specific tag name:

`az tag remove-value --name {{tag_name}} --value {{tag_value}}`
