#bru

> CLI Bruno-ի համար, Opensource IDE API-ների ուսումնասիրման և փորձարկման համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.usebruno.com/bru-cli/overview>:.

- Գործարկեք բոլոր հարցումների ֆայլերը ընթացիկ գրացուցակից.:

`bru run`

- Գործարկեք մեկ հարցում ընթացիկ գրացուցակից՝ նշելով դրա ֆայլի անունը.:

`bru run {{file.bru}}`

- Գործարկել հարցումները՝ օգտագործելով միջավայրը.:

`bru run --env {{environment_name}}`

- Գործարկել հարցումները՝ օգտագործելով փոփոխական ունեցող միջավայր.:

`bru run --env {{environment_name}} --env-var {{variable_name}}={{variable_value}}`

- Գործարկեք հարցումը և հավաքեք արդյունքները ելքային ֆայլում.:

`bru run --output {{path/to/output.json}}`

- Ցուցադրել օգնությունը.:

`bru run --help`
