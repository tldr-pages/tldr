# bun pm փաթեթ

> Ստեղծեք `.tgz` արխիվ, որը պարունակում է այն ֆայլերը, որոնք կհրապարակվեն npm (նույն վարքագիծը, ինչ `npm pack`):.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/pm/cli/pm#pack>:.

- Ստեղծեք tarball ընթացիկ աշխատանքային տարածքից.:

`bun pm pack`

- Գործարկել բոլոր քայլերը՝ առանց tarball-ը սկավառակի վրա գրելու.:

`bun pm pack --dry-run`

- Պահպանեք tarball-ը որոշակի գրացուցակում.:

`bun pm pack --destination {{path/to/directory}}`

- Սահմանեք ճշգրիտ ֆայլի անունը tarball-ի համար.:

`bun pm pack --filename {{filename}}`

- Բաց թողեք նախնական փաթեթը, փոստային փաթեթը և պատրաստեք սցենարներ.:

`bun pm pack --ignore-scripts`

- Սահմանեք `gzip` սեղմման մակարդակը (0-9, լռելյայն՝ 9):

`bun pm pack --gzip-level 5`

- Արտադրեք միայն tarball ֆայլի անվանումը և ճնշեք բանավոր տեղեկամատյանները.:

`bun pm pack --quiet`
