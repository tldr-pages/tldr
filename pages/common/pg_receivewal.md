# pg_receivewal

> Streams the write-ahead log from a running PostgreSQL cluster.
> More information: <https://www.postgresql.org/docs/current/app-pgreceivewal.html>.

- Stream WAL to a local directory (minimum required):

`pg_receivewal {{[-D|--directory]}} {{directory}}`

- Same as above, specify host, port, username including verbose output:

`pg_receivewal --verbose -h {{host}} -p {{port}} -U {{username}} {{[-D|--directory]}} {{directory}}`

- Use replication slot (create-if-needed):

`pg_receivewal --slot={{slot_name}} --create-slot -h {{host}} -p {{port}} -U {{username}} {{[-D|--directory]}} {{directory}}`

- Stop at a given WAL position (LSN):

`pg_receivewal --endpos={{lsn}} {{[-D|--directory]}} {{directory}} -h {{host}} -p {{port}} -U {{username}}`

- Control looping on failure:

`pg_receivewal --no-loop {{[-D|--directory]}} {{directory}} -h {{host}} -p {{port}} -U {{username}}`

- Flush data synchronously (force WAL writes immediately):

`pg_receivewal --synchronous {{[-D|--directory]}} {{directory}} -h {{host}} -p {{port}} -U {{username}}`

- Compress WAL output (gzip, level 0–9):

`pg_receivewal --compress={{level}} {{[-D|--directory]}} {{directory}} -h {{host}} -p {{port}} -U {{username}}`

- Set status reporting interval:

`pg_receivewal --status-interval={{seconds}} {{[-D|--directory]}} {{directory}} -h {{host}} -p {{port}} -U {{username}}`
