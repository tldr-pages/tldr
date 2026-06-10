# az appconfig

> Կառավարեք հավելվածների կազմաձևերը Azure-ում:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/appconfig>:.

- Ստեղծեք հավելվածի կոնֆիգուրացիա.:

`az appconfig create {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{group_name}} {{[-l|--location]}} {{location}}`

- Ջնջել հատուկ հավելվածի կոնֆիգուրացիան.:

`az appconfig delete {{[-g|--resource-group]}} {{rg_name}} {{[-n|--name]}} {{appconfig_name}}`

- Թվարկեք բոլոր հավելվածների կազմաձևերը ընթացիկ բաժանորդագրության ներքո.:

`az appconfig list`

- Թվարկեք բոլոր հավելվածների կազմաձևերը որոշակի ռեսուրսների խմբի ներքո.:

`az appconfig list {{[-g|--resource-group]}} {{rg_name}}`

- Ցույց տալ հավելվածի կազմաձևման հատկությունները.:

`az appconfig show {{[-n|--name]}} {{appconfig_name}}`

- Թարմացրեք հատուկ հավելվածի կոնֆիգուրացիան.:

`az appconfig update {{[-g|--resource-group]}} {{rg_name}} {{[-n|--name]}} {{appconfig_name}}`
