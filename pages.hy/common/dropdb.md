# dropdb

> Հեռացնել PostgreSQL տվյալների բազան:.
> Պարզ փաթաթում SQL `DROP DATABASE` հրամանի շուրջ:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-dropdb.html>:.

- Ոչնչացնել տվյալների բազան.:

`dropdb {{database_name}}`

- Ցանկացած կործանարար գործողություններից առաջ պահանջեք ստուգման հուշում.:

`dropdb {{[-i|--interactive]}} {{database_name}}`

- Միացեք հատուկ օգտվողի անունով և ոչնչացրեք տվյալների բազան.:

`dropdb {{[-U|--username]}} {{username}} {{database_name}}`

- Տվյալների շտեմարանին միանալուց առաջ պարտադրել գաղտնաբառի հուշում.:

`dropdb {{[-W|--password]}} {{database_name}}`

- Տվյալների շտեմարանին միանալուց առաջ սեղմեք գաղտնաբառի հուշումը.:

`dropdb {{[-w|--no-password]}} {{database_name}}`

- Նշեք սերվերի հոսթի անունը.:

`dropdb {{[-h|--host]}} {{host}} {{database_name}}`

- Նշեք սերվերի նավահանգիստը.:

`dropdb {{[-p|--port]}} {{port}} {{database_name}}`

- Տվյալների բազան ոչնչացնելուց առաջ փորձեք դադարեցնել գոյություն ունեցող կապերը.:

`dropdb {{[-f|--force]}} {{database_name}}`
