# postgres

> Գործարկեք PostgreSQL տվյալների բազայի սերվերը:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-postgres.html>:.

- Գործարկեք սերվերը որոշակի նավահանգստի վրա (կանխադրված է 5432):

`postgres -p {{5433}}`

- Սահմանեք գործարկման ժամանակի պարամետր (կարճ ձև).:

`postgres -c {{shared_buffers=128MB}}`

- Սահմանեք գործարկման ժամանակի պարամետր (երկար ձև).:

`postgres --{{shared-buffers}}={{128MB}}`

- Սկսեք մեկ օգտատիրոջ ռեժիմով հատուկ տվյալների բազայի համար (կանխադրված է օգտագործողի անվան համար).:

`postgres --single -D {{path/to/datadir}} {{my_database}}`
