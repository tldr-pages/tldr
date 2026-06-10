# pg_checksums

> Միացնել, անջատել կամ ստուգել տվյալների ստուգման գումարները PostgreSQL տվյալների բազայի կլաստերում:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgchecksums.html>:.

- Ստուգեք տվյալների ստուգման գումարները տվյալների բազայի կլաստերում.:

`pg_checksums {{[-D|--pgdata]}} {{path/to/data}}`

- Միացնել տվյալների ստուգման գումարները տվյալների բազայի կլաստերում.:

`pg_checksums {{[-e|--enable]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Անջատեք տվյալների ստուգման գումարները տվյալների բազայի կլաստերում.:

`pg_checksums {{[-d|--disable]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Ստուգեք տվյալների ստուգման գումարները՝ մանրամասն ելքով.:

`pg_checksums {{[-v|--verbose]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Ստուգեք տվյալների ստուգման գումարները, որոնք ցույց են տալիս առաջընթացը.:

`pg_checksums {{[-P|--progress]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Ցուցադրել օգնությունը.:

`pg_checksums {{[-?|--help]}}`
