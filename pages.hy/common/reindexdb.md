# reindexdb

> Վերակառուցել ինդեքսները PostgreSQL տվյալների բազայում:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-reindexdb.html>:.

- Վերինդեքսավորել հատուկ տվյալների բազա.:

`reindexdb {{database_name}}`

- Հատուկ տվյալների բազայի վերաինդեքսավորում՝ օգտագործելով կապի ընտրանքները.:

`reindexdb {{database_name}} {{[-h|--host]}} {{hostname}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Վերինդեքսավորել բոլոր տվյալների բազաները.:

`reindexdb {{[-a|--all]}}`

- Վերինդեքսավորել հատուկ աղյուսակը տվյալների բազայում.:

`reindexdb {{database_name}} {{[-t|--table]}} {{table_name}}`

- Վերինդեքսավորել հատուկ ինդեքս տվյալների բազայում.:

`reindexdb {{database_name}} {{[-i|--index]}} {{index_name}}`

- Վերինդեքսավորել հատուկ սխեմա տվյալների բազայում.:

`reindexdb {{database_name}} {{[-S|--schema]}} {{schema_name}}`

- Վերինդեքսավորել բովանդակալից ելքով.:

`reindexdb {{database_name}} {{[-v|--verbose]}}`

- Վերինդեքսավորել տվյալների բազան՝ օգտագործելով բազմաթիվ զուգահեռ աշխատանքներ.:

`reindexdb {{database_name}} {{[-j|--jobs]}} {{number_of_jobs}}`
