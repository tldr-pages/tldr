# showmount

> Display mount information for an NFS server.
> More information: <https://manned.org/showmount>.

- Show clients currently mounting from the server:

`showmount {{hostname}}`

- Show the NFS server's export list:

`showmount {{[-e|--exports]}} {{hostname}}`

- Show all clients and their mounted directories:

`showmount {{[-a|--all]}} {{hostname}}`

- Show only the directories mounted by clients:

`showmount {{[-d|--directories]}} {{hostname}}`

- Show the export list without headers:

`showmount {{[-e|--exports]}} --no-headers {{hostname}}`

- Display help:

`showmount {{[-h|--help]}}`
