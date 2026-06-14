# pg_upgrade

> Թարմացրեք PostgreSQL տվյալների բազայի կլաստերը նոր հիմնական տարբերակի:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/pgupgrade.html>:.

- Ստուգեք կլաստերները թարմացումից առաջ.:

`pg_upgrade {{[-c|--check]}} {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}}`

- Կատարեք իրական արդիականացում.:

`pg_upgrade {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}}`

- Թարմացման ընթացքում օգտագործեք մի քանի զուգահեռ աշխատանքներ.:

`pg_upgrade {{[-j|--jobs]}} {{njobs}} {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}}`

- Նշեք հին և նոր PostgreSQL նավահանգիստները.:

`pg_upgrade {{[-p|--old-port]}} {{port}} {{[-P|--new-port]}} {{port}} {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}}`

- Նոր կլաստերում ֆայլերը պատճենելու փոխարեն օգտագործեք կոշտ հղումներ.:

`pg_upgrade {{[-k|--link]}} {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}}`

- Ցուցադրել օգնությունը.:

`pg_upgrade {{[-?|--help]}}`
