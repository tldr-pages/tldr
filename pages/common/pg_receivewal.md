# pg_receivewal

> Stream the write-ahead log from a running PostgreSQL cluster.
> More information: <https://www.postgresql.org/docs/current/app-pgreceivewal.html>.

- Stream WAL to a local directory (minimum required):

`pg_receivewal {{[-D|--directory]}} {{path/to/directory}}`

- Same as above, specify host, port, username including verbose output:

`pg_receivewal {{[-D|--directory]}} {{path/to/directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-v|--verbose]}}`

- Use replication slot (create-if-needed):

`pg_receivewal {{[-D|--directory]}} {{path/to/directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-S|--slot]}} {{slot_name}} --create-slot`

- Stop at a given WAL position (LSN):

`pg_receivewal {{[-D|--directory]}} {{path/to/directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-E|--endpos]}} {{lsn}}`

- Control looping on failure:

`pg_receivewal {{[-D|--directory]}} {{path/to/directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-n|--no-loop]}}`

- Flush data synchronously (force WAL writes immediately):

`pg_receivewal {{[-D|--directory]}} {{path/to/directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} --synchronous`

- Compress WAL output (`gzip`, level 0-9):

`pg_receivewal {{[-D|--directory]}} {{path/to/directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-Z|--compress]}} {{level|method}}`

- Set status reporting interval:

`pg_receivewal {{[-D|--directory]}} {{path/to/directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-s|--status-interval]}} {{seconds}}`
