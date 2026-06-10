# լիչի

> Գտեք կոտրված URL-ներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/lycheeverse/lychee/blob/master/README.md#commandline-usage>:.

- Սկանավորեք կայքը կոտրված հղումների համար.:

`lychee {{https://example.com}}`

- Ցուցադրել սխալների տեսակների բաժանումը.:

`lychee --format detailed {{https://example.com}}`

- Սահմանափակեք կապերի քանակը՝ DDOS պաշտպանությունը կանխելու համար.:

`lychee --max-concurrency {{5}} {{links.txt}}`

- Ստուգեք ֆայլերը գրացուցակի կառուցվածքում ցանկացած կոտրված URL-ների համար.:

`grep {{[-r|--recursive]}} "{{pattern}}" | lychee -`

- Ցուցադրել օգնությունը.:

`lychee --help`
