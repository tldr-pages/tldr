# az cognitiveservices

> Gestisce gli account Azure Cognitive Services.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/cognitiveservices>.

- Crea un account Cognitive Services API in una posizione specifica senza conferma richiesta:

`az cognitiveservices account create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --kind {{api_name}} {{[-l|--location]}} {{location}} --sku {{sku_name}} --yes`

- Elenca gli utilizzi per l'account Azure Cognitive Services:

`az cognitiveservices account list-usage {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}}`

- Crea un deployment per l'account Azure Cognitive Services:

`az cognitiveservices account deployment create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --deployment-name {{deploy_name}} --model-name {{model_name}} --model-version "{{model_version}}" --model-format {{format_name}}`

- Crea un piano di commitment per l'account Azure Cognitive Services:

`az cognitiveservices account commitment-plan create {{[-n|--name]}} {{account_name}} {{[-g|--resource-group]}} {{resource_group}} --commitment-plan-name "{{plan_name}}" --hosting-model "{{hosting_model}}" --plan-type "{{plan_type}}" --auto-renew {{false|true}}`

- Elimina un piano di commitment dall'account Azure Cognitive Services:

`az cognitiveservices account commitment-plan delete {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{account_name}} --commitment-plan-name "{{plan_name}}"`
