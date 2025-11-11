# az cognitiveservices

> Manage Azure Cognitive Services accounts.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/cognitiveservices>.

- Create an API Cognitive Services account in a specific location without confirmation required:

`az cognitiveservices account create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --kind {{API_name}} {{[-l|--location]}} {{location}} --sku {{sku_name}} --yes`

- List usages for Azure Cognitive Services account:

`az cognitiveservices account list-usage {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}}`

- Create a deployment for Azure Cognitive Services account:

`az cognitiveservices account deployment create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --deployment-name {{deploy_name}} --model-name {{model_name}} --model-version "{{model_version}}" --model-format {{format_name}}`

- Create a commitment plan for Azure Cognitive Services account:

`az cognitiveservices account commitment-plan create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --commitment-plan-name "{{plan_name}}" --hosting-model "{{hosting_model}}" --plan-type "{{plan_type}}" --auto-renew {{false|true}}`

- Delete a commitment plan from Azure Cognitive Services account:

`az cognitiveservices account commitment-plan delete {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{account_name}} --commitment-plan-name "{{plan_name}}"`
