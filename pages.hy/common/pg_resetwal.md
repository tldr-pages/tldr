# pg_resetwal

> Վերականգնել PostgreSQL տվյալների բազայի կլաստերի նախօրոք գրելու գրանցամատյանը և կառավարման այլ տեղեկությունները:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgresetwal.html>:.

- Վերականգնել WAL-ը և վերահսկել տեղեկատվությունը որոշակի տվյալների գրացուցակի համար.:

`pg_resetwal {{[-D|--pgdata]}} {{path/to/data}}`

- Կատարել չոր վազք.:

`pg_resetwal {{[-D|--pgdata]}} {{path/to/data}} {{[-n|--dry-run]}}`

- Ստիպել WAL-ի և հսկողության տեղեկատվության վերակայումը.:

`pg_resetwal {{[-D|--pgdata]}} {{path/to/data}} {{[-f|--force]}}`

- Ցուցադրել օգնությունը.:

`pg_resetwal {{[-?|--help]}}`

- Ցուցադրման տարբերակը:

`pg_resetwal {{[-V|--version]}}`
