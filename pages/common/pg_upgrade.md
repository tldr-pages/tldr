# pg_upgrade

> Upgrade a PostgreSQL database cluster to a new major version.
> More information: <https://www.postgresql.org/docs/current/pgupgrade.html>.

- Check clusters before upgrading:

`pg_upgrade {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}} {{[-c|--check]}}`

- Perform the actual upgrade:

`pg_upgrade {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}}`

- Use multiple parallel jobs during the upgrade:

`pg_upgrade {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}} {{[-j|--jobs]}} {{number_of_jobs}}`

- Specify the old and new PostgreSQL ports:

`pg_upgrade {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}} {{[-p|--old-port]}} {{old_port}} {{[-P|--new-port]}} {{new_port}}`

- Use hard links instead of copying files to the new cluster:

`pg_upgrade {{[-b|--old-bindir]}} {{path/to/old_bin}} {{[-B|--new-bindir]}} {{path/to/new_bin}} {{[-d|--old-datadir]}} {{path/to/old_data}} {{[-D|--new-datadir]}} {{path/to/new_data}} {{[-k|--link]}}`

- Display help:

`pg_upgrade {{[-?|--help]}}`
