# pg_amcheck

> Ստուգեք կոռուպցիայի առկայությունը մեկ կամ մի քանի PostgreSQL տվյալների բազաներում:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgamcheck.html>:.

- Ստուգեք հատուկ տվյալների բազա.:

`pg_amcheck {{dbname}}`

- Ստուգեք բոլոր տվյալների բազաները.:

`pg_amcheck {{[-a|--all]}}`

- Ստուգեք տվյալների բազաները, որոնք համապատասխանում են նշված օրինակին.:

`pg_amcheck {{[-d|--database]}} {{pattern}}`

- Ստուգեք հատուկ աղյուսակները տվյալների բազայում.:

`pg_amcheck {{[-t|--table]}} {{pattern}} {{dbname}}`

- Ստուգեք հատուկ սխեմաներ տվյալների բազայում.:

`pg_amcheck {{[-s|--schema]}} {{pattern}} {{dbname}}`

- Ցուցադրել օգնությունը.:

`pg_amcheck {{[-?|--help]}}`
