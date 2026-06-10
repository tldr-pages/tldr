# ազ ապիմ

> Կառավարեք Azure API կառավարման ծառայությունները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/apim>:.

- Թվարկեք API կառավարման ծառայությունները ռեսուրսների խմբի շրջանակներում.:

`az apim list {{[-g|--resource-group]}} {{resource_group}}`

- Ստեղծեք API կառավարման ծառայության օրինակ.:

`az apim create {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} --publisher-email {{email}} --publisher-name {{name}}`

- Ջնջել API կառավարման ծառայությունը.:

`az apim delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Ցույց տալ API կառավարման ծառայության օրինակի մանրամասները.:

`az apim show {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Թարմացրեք API կառավարման ծառայության օրինակը.:

`az apim update {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`
