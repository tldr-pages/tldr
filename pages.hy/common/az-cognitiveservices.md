# az ճանաչողական ծառայություններ

> Կառավարեք Azure Cognitive Services հաշիվները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/cognitiveservices>:.

- Ստեղծեք API Cognitive Services հաշիվ կոնկրետ վայրում՝ առանց հաստատման պահանջի.:

`az cognitiveservices account create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --kind {{api_name}} {{[-l|--location]}} {{location}} --sku {{sku_name}} --yes`

- Ցուցակե՛ք Azure Cognitive Services-ի կիրառությունները.:

`az cognitiveservices account list-usage {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}}`

- Ստեղծեք տեղակայում Azure Cognitive Services հաշվի համար.:

`az cognitiveservices account deployment create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --deployment-name {{deploy_name}} --model-name {{model_name}} --model-version "{{model_version}}" --model-format {{format_name}}`

- Ստեղծեք պարտավորությունների պլան Azure Cognitive Services հաշվի համար.:

`az cognitiveservices account commitment-plan create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --commitment-plan-name "{{plan_name}}" --hosting-model "{{hosting_model}}" --plan-type "{{plan_type}}" --auto-renew {{false|true}}`

- Ջնջել պարտավորությունների պլանը Azure Cognitive Services հաշվից.:

`az cognitiveservices account commitment-plan delete {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{account_name}} --commitment-plan-name "{{plan_name}}"`
