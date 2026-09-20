# unshare

> Execute a command in new user-defined namespaces.
> More information: <https://manned.org/unshare>.

- Execute the default shell:

`unshare`

- Execute a command without sharing access to connected networks:

`sudo unshare {{[-n|--net]}} {{command}} {{argument1 argument2 ...}}`

- Execute a command as a child process without sharing mounts, processes, or networks:

`sudo unshare {{[-mpnf|--mount --pid --net --fork]}} {{command}} {{argument1 argument2 ...}}`

- Create a container manually:

`sudo unshare {{[-puinmf|--pid --uts --ipc --net --mount --fork]}} chroot {{path/to/new_root}} {{/bin/sh}}`
