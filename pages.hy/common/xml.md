# xml

> XMLStarlet Toolkit. հարցում, խմբագրում, ստուգում, փոխակերպում և վերափոխում XML փաստաթղթերը:.
> Որոշ ենթահրամաններ, ինչպիսիք են `validate`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139670224>:.

- Ցուցադրել ընդհանուր օգնությունը, ներառյալ ենթահրամանների ցանկը.:

`xml --help`

- Կատարեք ենթահրաման՝ ֆայլից կամ URI-ից մուտքագրելով՝ տպելով `stdout`:

`xml {{subcommand}} {{options}} {{path/to/input.xml|uri}}`

- Կատարեք ենթահրաման՝ օգտագործելով `stdin` և `stdout`:

`xml {{subcommand}} {{options}}`

- Կատարեք ենթահրաման՝ մուտքագրելով ֆայլից կամ URI-ից և դուրս բերեք ֆայլ.:

`xml {{subcommand}} {{options}} {{path/to/input.xml|uri}} > {{path/to/output}}`

- Ցուցադրել օգնություն կոնկրետ ենթահրամանի համար.:

`xml {{subcommand}} --help`

- Ցուցադրման տարբերակը:

`xml --version`
