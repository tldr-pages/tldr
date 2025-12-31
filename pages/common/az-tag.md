# az tag

> Manage tags on a resource.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/tag>.

- Create a tag value:

`az tag add-value {{[-n|--name]}} {{tag_name}} --value {{tag_value}}`

- Create a tag in the subscription:

`az tag create {{[-n|--name]}} {{tag_name}}`

- Delete a tag from the subscription:

`az tag delete {{[-n|--name]}} {{tag_name}}`

- List all tags on a subscription:

`az tag list --resource-id /subscriptions/{{subscription_id}}`

- Delete a tag value for a specific tag name:

`az tag remove-value {{[-n|--name]}} {{tag_name}} --value {{tag_value}}`
