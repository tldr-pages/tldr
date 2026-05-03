# unshare

> Execute a command in new user-defined namespaces.
> More information: <https://manned.org/unshare>.

- Execute the default shell:

`unshare`

- Execute a command without sharing access to connected networks:

`sudo unshare {{[-n|--net]}} {{command}} {{command_arguments}}`

- Execute a command as a child process without sharing mounts, processes, or networks:

`sudo unshare {{[-m|--mount]}} {{[-i|--pid]}} {{[-n|--net]}} {{[-f|--fork]}} {{command}} {{command_arguments}}`
