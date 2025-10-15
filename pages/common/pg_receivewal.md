# pg_receivewal

> Stream the write-ahead log from a running PostgreSQL cluster.
> More information: <https://www.postgresql.org/docs/current/app-pgreceivewal.html>.

- Stream WAL to a local directory (minimum required):

`pg_receivewal {{[-D|--directory]}} {{directory}}`

- Same as above, specify host, port, username including verbose output:

`pg_receivewal {{[-v|--verbose]}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-D|--directory]}} {{directory}}`

- Use replication slot (create-if-needed):

`pg_receivewal {{[-S|--slot]}} {{slot_name}} --create-slot {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-D|--directory]}} {{directory}}`

- Stop at a given WAL position (LSN):

`pg_receivewal {{[-E|--endpos]}} {{lsn}} {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Control looping on failure:

`pg_receivewal {{[-n|--no-loop]}} {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Flush data synchronously (force WAL writes immediately):

`pg_receivewal --synchronous {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Compress WAL output (gzip, level 0–9):

`pg_receivewal {{[-Z|--compress]}} {{level|method}} {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Set status reporting interval:

`pg_receivewal {{[-s|--status-interval]}} {{seconds}} {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`
