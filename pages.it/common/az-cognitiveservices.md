# az cognitiveservices

> Gestisce gli account Azure Cognitive Services.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/cognitiveservices>.

- Crea un account Cognitive Services API in una posizione specifica senza conferma richiesta:

`az cognitiveservices account create {{[-n|--name]}} {{nome_account}} {{[-g|--resource-group]}} {{gruppo_risorse}} --kind {{nome_API}} {{[-l|--location]}} {{posizione}} --sku {{nome_sku}} --yes`

- Elenca gli utilizzi per l'account Azure Cognitive Services:

`az cognitiveservices account list-usage {{[-n|--name]}} {{nome_account}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Crea un deployment per l'account Azure Cognitive Services:

`az cognitiveservices account deployment create {{[-n|--name]}} {{nome_account}} {{[-g|--resource-group]}} {{gruppo_risorse}} --deployment-name {{nome_deploy}} --model-name {{nome_modello}} --model-version "{{versione_modello}}" --model-format {{nome_formato}}`

- Crea un piano di commitment per l'account Azure Cognitive Services:

`az cognitiveservices account commitment-plan create {{[-n|--name]}} {{nome_account}} {{[-g|--resource-group]}} {{gruppo_risorse}} --commitment-plan-name "{{nome_piano}}" --hosting-model "{{modello_hosting}}" --plan-type "{{tipo_piano}}" --auto-renew {{false|true}}`

- Elimina un piano di commitment dall'account Azure Cognitive Services:

`az cognitiveservices account commitment-plan delete {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome_account}} --commitment-plan-name "{{nome_piano}}"`
