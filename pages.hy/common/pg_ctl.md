# pg_ctl

> PostgreSQL սերվերի և տվյալների բազայի կլաստերի կառավարման համար օգտակար ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pg-ctl.html>:.

- Նախաձեռնեք նոր PostgreSQL տվյալների բազայի կլաստերը.:

`pg_ctl {{[-D|--pgdata]}} {{data_directory}} init`

- Սկսեք PostgreSQL սերվեր.:

`pg_ctl {{[-D|--pgdata]}} {{data_directory}} start`

- Դադարեցրեք PostgreSQL սերվերը.:

`pg_ctl {{[-D|--pgdata]}} {{data_directory}} stop`

- Վերագործարկեք PostgreSQL սերվերը.:

`pg_ctl {{[-D|--pgdata]}} {{data_directory}} restart`

- Վերբեռնեք PostgreSQL սերվերի կազմաձևումը.:

`pg_ctl {{[-D|--pgdata]}} {{data_directory}} reload`
