#սպասել4x

> Սպասեք, որ նավահանգիստը կամ ծառայությունը մտնի պահանջվող վիճակ՝ TCP, HTTP, DNS, տվյալների բազաների և հաղորդագրությունների հերթերի աջակցությամբ:.
> Որոշ ենթահրամաններ, ինչպիսիք են `tcp`-ը և `http`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/wait4x/wait4x>:.

- Սպասեք, մինչև TCP պորտը հասանելի դառնա.:

`wait4x tcp {{localhost:8080}}`

- Սպասեք մինչև HTTP վերջնակետը վերադարձնի որոշակի կարգավիճակի կոդը.:

`wait4x http {{https://example.com/health}} --expect-status-code {{200}}`

- Սպասեք, մինչև PostgreSQL տվյալների բազան պատրաստ դառնա.:

`wait4x postgresql '{{postgres://user:password@localhost:5432/mydb?sslmode=disable}}'`

- Սպասեք, մինչև Redis սերվերը հասանելի դառնա.:

`wait4x redis {{redis://localhost:6379}}`

- Սպասեք ծառայության մաքսային ժամանակի ավարտով և ստուգեք ընդմիջումը.:

`wait4x tcp {{localhost:3306}} --timeout {{30s}} --interval {{2s}}`

- Սպասեք մի քանի ծառայությունների զուգահեռ.:

`wait4x tcp {{localhost:3306 localhost:6379 ...}}`

- Ցուցադրել օգնություն ենթահրամանի համար.:

`wait4x {{subcommand}} --help`

- Ցուցադրման տարբերակը:

`wait4x version`
