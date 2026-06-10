# pg_wind

> Համաժամացրեք PostgreSQL տվյալների գրացուցակը մեկ այլ տվյալների գրացուցակի հետ, որը պատառաքաղված է դրանից:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgrewind.html>:.

- Սինքրոնացրեք թիրախային գրացուցակը աղբյուրի գրացուցակի հետ.:

`pg_rewind {{[-D|--target-pgdata]}} {{path/to/target_data}} --source-pgdata {{path/to/source_data}}`

- Սինքրոնացրեք թիրախը աղբյուրի սերվերի հետ՝ օգտագործելով կապի տողը.:

`pg_rewind {{[-D|--target-pgdata]}} {{path/to/target_data}} --source-server {{connstr}}`

- Կատարել չոր վազք.:

`pg_rewind {{[-D|--target-pgdata]}} {{path/to/target_data}} --source-pgdata {{path/to/source_data}} {{[-n|--dry-run]}}`

- Ցույց տալ առաջընթացը համաժամացման ընթացքում.:

`pg_rewind {{[-D|--target-pgdata]}} {{path/to/target_data}} --source-pgdata {{path/to/source_data}} {{[-P|--progress]}}`

- Ցուցադրել օգնությունը.:

`pg_rewind {{[-?|--help]}}`
