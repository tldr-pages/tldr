# pg_waldump

> Ցուցադրել PostgreSQL տվյալների բազայի կլաստերի մարդու կողմից ընթեռնելի մատյանի (WAL) արտապատկերումը:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/pgwaldump.html>:.

- Ցուցադրել WAL գրառումները որոշակի հատվածից.:

`pg_waldump {{start_segment}}`

- Ցուցադրել WAL գրառումները երկու հատվածների միջև.:

`pg_waldump {{start_segment}} {{end_segment}}`

- Նշեք WAL ֆայլի գրացուցակը.:

`pg_waldump {{start_segment}} {{end_segment}} {{[-p|--path]}} {{path}}`

- Հետևեք նոր WAL գրառումներին, երբ նրանք հասնում են.:

`pg_waldump {{start_segment}} {{end_segment}} {{[-f|--follow]}}`

- Ցուցադրված գրառումների քանակի սահմանափակում.:

`pg_waldump {{start_segment}} {{end_segment}} {{[-n|--limit]}} {{count}}`

- Ցուցադրել ամփոփ վիճակագրություն անհատական գրառումների փոխարեն.:

`pg_waldump {{start_segment}} {{end_segment}} {{[-z|--stats]}}`

- Զտել ըստ ռեսուրսների կառավարչի.:

`pg_waldump {{start_segment}} {{end_segment}} {{[-r|--rmgr]}} {{rmgr_name}}`

- Ցուցադրել օգնությունը.:

`pg_waldump {{[-?|--help]}}`
