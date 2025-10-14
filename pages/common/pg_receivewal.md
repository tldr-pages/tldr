# pg_receivewal

> Streams the write-ahead log from a running PostgreSQL cluster.
> More information: <https://www.postgresql.org/docs/current/app-pgreceivewal.html>.

- Stream WAL to a local directory (minimum required):

  `pg_receivewal -D {{directory}}`

- Same as above, specify host, port, username:

  `pg_receivewal -h {{host}} -p {{port}} -U {{username}} -D {{directory}}`

- Include verbose output:

  `pg_receivewal --verbose -h {{host}} -p {{port}} -U {{username}} -D {{directory}}`

- Use replication slot (create-if-needed):

  `pg_receivewal --slot={{slot_name}} --create-slot -h {{host}} -p {{port}} -U {{username}} -D {{directory}}`

- Drop a replication slot:

  `pg_receivewal --slot={{slot_name}} --drop-slot -h {{host}} -p {{port}} -U {{username}}`

- Stop at a given WAL position (LSN):

  `pg_receivewal --endpos={{lsn}} -D {{directory}} -h {{host}} -p {{port}} -U {{username}}`

- Control looping on failure:

  `pg_receivewal --no-loop -D {{directory}} -h {{host}} -p {{port}} -U {{username}}`

- Flush data synchronously (force WAL writes immediately):

  `pg_receivewal --synchronous -D {{directory}} -h {{host}} -p {{port}} -U {{username}}`

- Disable forcing sync to disk (faster but riskier):

  `pg_receivewal --no-sync -D {{directory}}`

- Compress WAL output (gzip, level 0–9):

  `pg_receivewal --compress={{level}} -D {{directory}} -h {{host}} -p {{port}} -U {{username}}`

- Set status reporting interval:

  `pg_receivewal --status-interval={{seconds}} -D {{directory}} -h {{host}} -p {{port}} -U {{username}}`
