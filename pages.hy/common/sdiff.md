# sdiff

> Համեմատեք տարբերությունները և ընտրովի միացրեք 2 ֆայլ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sdiff>:.

- Համեմատեք 2 ֆայլ.:

`sdiff {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք 2 ֆայլ՝ անտեսելով բոլոր ներդիրներն ու բացատները.:

`sdiff {{[-W|--ignore-all-space]}} {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք 2 ֆայլ՝ անտեսելով տողերի վերջում բացատը.:

`sdiff {{[-Z|--ignore-trailing-space]}} {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք 2 ֆայլ՝ մեծատառերի անզգայուն եղանակով.:

`sdiff {{[-i|--ignore-case]}} {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք և այնուհետև միաձուլեք՝ ելքը գրելով նոր ֆայլի մեջ.:

`sdiff {{[-o|--output]}} {{path/to/merged_file}} {{path/to/file1}} {{path/to/file2}}`
