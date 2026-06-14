# az տրամաբանական հավելված

> Կառավարեք տրամաբանական հավելվածները Azure Cloud ծառայություններում:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/logicapp>:.

- Ստեղծեք տրամաբանական ծրագիր.:

`az logicapp create {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} {{[-s|--storage-account]}} {{storage_account}}`

- Ջնջել տրամաբանական հավելվածը.:

`az logicapp delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Ցուցակեք տրամաբանական հավելվածները.:

`az logicapp list {{[-g|--resource-group]}} {{resource_group}}`

- Վերագործարկեք տրամաբանական հավելվածը.:

`az logicapp restart {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Սկսեք տրամաբանական ծրագիր.:

`az logicapp start {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Դադարեցրեք տրամաբանական հավելվածը.:

`az logicapp stop {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`
