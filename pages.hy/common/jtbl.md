# jtbl

> JSON և JSON Lines-ի տվյալները տերմինալում որպես աղյուսակ տպելու օգտակար ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://github.com/kellyjonbrazil/jtbl#usage>:.

- Տպեք աղյուսակ JSON կամ JSON Lines մուտքագրումից.:

`cat {{file.json}} | jtbl`

- Տպեք աղյուսակ և նշեք սյունակի լայնությունը փաթաթման համար.:

`cat {{file.json}} | jtbl --cols={{width}}`

- Տպեք աղյուսակ և կրճատեք տողերը փաթաթելու փոխարեն.:

`cat {{file.json}} | jtbl {{[-t|--truncate]}}`

- Տպեք աղյուսակ և մի փաթաթեք կամ կտրեք տողերը.:

`cat {{file.json}} | jtbl {{[-n|--no-wrap]}}`
