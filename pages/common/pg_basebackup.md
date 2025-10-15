# pg_basebackup

> Take a base backup of a running PostgreSQL cluster.
> Used for full or incremental backups, point-in-time recovery, or setting up replication standbys.
> More information: <https://www.postgresql.org/docs/current/app-pgbasebackup.html>.

- Take a base backup from a remote PostgreSQL server:

`pg_basebackup {{[-h|--host]}} {{host}} {{[-D|--pgdata]}} {{path/to/backup_dir}}`

- Take a backup with progress shown:

`pg_basebackup {{[-h|--host]}} {{host}} {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-P|--progress]}}`

- Create a compressed backup (`gzip`) in tar format:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-F|--format]}} {{[t|tar]}} {{[-z|--gzip]}}`

- Create an incremental backup using a previous manifest file:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-i|--incremental]}} {{path/to/old_manifest}}`

- Write a recovery configuration for setting up a standby:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-R|--write-recovery-conf]}}`

- Relocate a tablespace during backup:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-T|--tablespace-mapping]}} {{path/to/old_tablespace}}={{path/to/new_tablespace}}`

- Limit transfer rate to reduce server load:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-r|--max-rate]}} {{100M}}`

- Stream WAL logs while taking the backup:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-X|--wal-method]}} stream`
