# az cognitiveservices

> 管理 Azure 认知服务账户。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/cognitiveservices>.

- 在指定位置创建一个 API Azure 认知服务账户，且无需确认：

`az cognitiveservices account create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --kind {{API_name}} {{[-l|--location]}} {{location}} --sku {{sku_name}} --yes`

- 列出 Azure 认知服务账户的使用情况：

`az cognitiveservices account list-usage {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}}`

- 为 Azure 认知服务账户创建一个部署：

`az cognitiveservices account deployment create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --deployment-name {{deploy_name}} --model-name {{model_name}} --model-version "{{model_version}}" --model-format {{format_name}}`

- 为 Azure 认知服务账户创建一个承诺计划：

`az cognitiveservices account commitment-plan create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --commitment-plan-name "{{plan_name}}" --hosting-model "{{hosting_model}}" --plan-type "{{plan_type}}" --auto-renew {{false|true}}`

- 从 Azure 认知服务账户中删除一个承诺计划：

`az cognitiveservices account commitment-plan delete {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{account_name}} --commitment-plan-name "{{plan_name}}"`
