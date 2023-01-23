# az tag

> Címkék kezelése egy erőforráson. A `azure-cli` része. További információ: <https://learn.microsoft.com/cli/azure/tag>.

- Címkeérték létrehozása:

`az tag add-value --name {{tag_name}} --value {{tag_value}}`

- Hozzon létre egy címkét az előfizetésben:

`az tag create --name {{tag_name}}`

- Címke törlése az előfizetésből:

`az tag delete --name {{tag_name}}`

- Az előfizetés összes címkéjének listázása:

`az tag list --resource-id /subscriptions/{{subscription_id}}`

- Címkeérték törlése egy adott címkenévhez:

`az tag remove-value --name {{tag_name}} --value {{tag_value}}`
