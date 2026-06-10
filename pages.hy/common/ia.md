#իա

> Գործիք՝ `archive.org`-ի հետ փոխազդելու համար:.
> Լրացուցիչ տեղեկություններ. <https://archive.org/developers/internetarchive/cli.html>:.

- Կարգավորեք `ia`-ը API ստեղներով (որոշ գործառույթներ չեն աշխատի առանց այս քայլի).:

`ia configure`

- Վերբեռնեք մեկ կամ մի քանի տարր `archive.org`՝:

`ia upload {{identifier}} {{path/to/file}} --metadata="{{mediatype:data}}" --metadata="{{title:example}}"`

- Ներբեռնեք մեկ կամ մի քանի տարրեր `archive.org`-ից՝:

`ia download {{item}}`

- Ջնջել մեկ կամ մի քանի տարրեր `archive.org`-ից.:

`ia delete {{identifier}} {{file}}`

- Որոնեք `archive.org`-ում, արդյունքները վերադարձնելով որպես JSON:

`ia search '{{subject:"subject" collection:collection}}'`
