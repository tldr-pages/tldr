# sui քայլ

> Աշխատեք «Տեղափոխել» աղբյուրի կոդի հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.sui.io/references/cli/move>:.

- Ստեղծեք նոր Move նախագիծ տվյալ թղթապանակում.:

`sui move new {{project_name}}`

- Փորձարկեք Move նախագիծը ընթացիկ գրացուցակում.:

`sui move test`

- Փորձարկեք ծածկույթով և ստացեք ամփոփում.:

`sui move test --coverage; sui move coverage summary`

- Գտեք ձեր կոդի որ մասերն են ծածկված թեստերից (այսինքն՝ բացատրեք ծածկույթի արդյունքները).:

`sui move coverage source --module {{module_name}}`

- Կառուցեք Move նախագիծը ընթացիկ գրացուցակում.:

`sui move build`

- Կառուցեք Move նախագիծը տվյալ ճանապարհից.:

`sui move build --path {{path}}`

- Տեղափոխեք դեպի Տեղափոխեք 2024 փաթեթը տրամադրված ճանապարհով.:

`sui move migrate {{path}}`
