# unshare

> Execute a command in new user-defined namespaces.
> More information: <https://www.kernel.org/doc/html/latest/userspace-api/unshare.html>.

- Execute a command without sharing access to connected networks:

`unshare --net {{command}} {{command_arguments}}`

- Execute a command as a child process without sharing mounts, processes, or networks:

`unshare --mount --pid --net --fork {{command}} {{command_arguments}}`
