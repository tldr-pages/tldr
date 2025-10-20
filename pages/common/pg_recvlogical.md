# pg_recvlogical

> Control PostgreSQL logical decoding streams.
> More information: <https://www.postgresql.org/docs/current/app-pgrecvlogical.html>.

- Create a new logical replication slot:

`pg_recvlogical {{[-d|--dbname]}} {{dbname}} {{[-S|--slot]}} {{slot_name}} --create-slot`

- Start streaming changes from a logical replication slot to a file:

`pg_recvlogical {{[-d|--dbname]}} {{dbname}} {{[-S|--slot]}} {{slot_name}} --start {{[-f|--file]}} {{filename}}`

- Drop a logical replication slot:

`pg_recvlogical {{[-d|--dbname]}} {{dbname}} {{[-S|--slot]}} {{slot_name}} --drop-slot`

- Create a slot with two-phase commit enabled:

`pg_recvlogical {{[-d|--dbname]}} {{dbname}} {{[-S|--slot]}} {{slot_name}} --create-slot {{[-t|--enable-two-phase]}}`

- Display help:

`pg_recvlogical {{[-?|--help]}}`
