# pg_upgrade

> Upgrade a PostgreSQL database cluster to a new major version.
> More information: <https://www.postgresql.org/docs/current/pgupgrade.html>.

- Check clusters before upgrading:

`pg_upgrade {{[-c|--check]}} {{[-b|--old-bindir]}} {{path/to/old/bin}} {{[-B|--new-bindir]}} {{path/to/new/bin}} {{[-d|--old-datadir]}} {{path/to/old/data}} {{[-D|--new-datadir]}} {{path/to/new/data}}`

- Perform the actual upgrade:

`pg_upgrade {{[-b|--old-bindir]}} {{path/to/old/bin}} {{[-B|--new-bindir]}} {{path/to/new/bin}} {{[-d|--old-datadir]}} {{path/to/old/data}} {{[-D|--new-datadir]}} {{path/to/new/data}}`

- Use multiple parallel jobs during the upgrade:

`pg_upgrade {{[-j|--jobs]}} {{njobs}} {{[-b|--old-bindir]}} {{path/to/old/bin}} {{[-B|--new-bindir]}} {{path/to/new/bin}} {{[-d|--old-datadir]}} {{path/to/old/data}} {{[-D|--new-datadir]}} {{path/to/new/data}}`

- Specify the old and new PostgreSQL ports:

`pg_upgrade {{[-p|--old-port]}} {{port}} {{[-P|--new-port]}} {{port}} {{[-b|--old-bindir]}} {{path/to/old/bin}} {{[-B|--new-bindir]}} {{path/to/new/bin}} {{[-d|--old-datadir]}} {{path/to/old/data}} {{[-D|--new-datadir]}} {{path/to/new/data}}`

- Use hard links instead of copying files to the new cluster:

`pg_upgrade {{[-k|--link]}} {{[-b|--old-bindir]}} {{path/to/old/bin}} {{[-B|--new-bindir]}} {{path/to/new/bin}} {{[-d|--old-datadir]}} {{path/to/old/data}} {{[-D|--new-datadir]}} {{path/to/new/data}}`

- Display help:

`pg_upgrade {{[-?|--help]}}`
