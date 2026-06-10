# լամբո նոր

> Գերհզոր `laravel new` Laravel-ի և Valet-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tighten/lambo#lambo-commands>:.

- Ստեղծեք նոր Laravel հավելված.:

`lambo new {{app_name}}`

- Տեղադրեք հավելվածը հատուկ ճանապարհով.:

`lambo new {{[-p|--path]}} {{path/to/directory}} {{app_name}}`

- Ներառեք նույնականացման փայտամածներ.:

`lambo new --auth {{app_name}}`

- Ներառեք հատուկ ճակատ.:

`lambo new --{{vue|bootstrap|react}} {{app_name}}`

- Տեղադրեք `npm` կախվածությունները նախագիծը ստեղծելուց հետո.:

`lambo new --node {{app_name}}`

- Նախագիծը ստեղծելուց հետո ստեղծեք Valet կայք.:

`lambo new {{[-l|--link]}} {{app_name}}`

- Ստեղծեք նոր MySQL տվյալների բազա՝ նույն անունով, ինչ նախագիծը.:

`lambo new --create-db --dbuser={{user}} --dbpassword={{password}} {{app_name}}`

- Նախագիծը ստեղծելուց հետո բացեք հատուկ խմբագիր.:

`lambo new {{[-e|--editor]}} "{{editor}}" {{app_name}}`
