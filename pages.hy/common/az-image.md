# ազ պատկեր

> Կառավարեք հատուկ վիրտուալ մեքենայի պատկերները Azure-ում:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/image>:.

- Թվարկեք հարմարեցված պատկերները ռեսուրսների խմբի տակ.:

`az image list {{[-g|--resource-group]}} {{resource_group}}`

- Ստեղծեք հարմարեցված պատկեր կառավարվող սկավառակներից կամ նկարներից.:

`az image create {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}} --os-type {{windows|linux}} --source {{os_disk_source}}`

- Ջնջել հատուկ պատկեր.:

`az image delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Ցույց տալ հատուկ պատկերի մանրամասները.:

`az image show {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Թարմացրեք մաքսային պատկերները.:

`az image update {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} --set {{property=value}}`
