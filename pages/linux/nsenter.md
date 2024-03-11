# nsenter

> Run a new command in a running process' namespace.
> Particularly useful for Docker images or chroot jails.
> More information: <https://manned.org/nsenter>.

- Run a specific command using the same namespaces as an existing process:

`nsenter --target {{pid}} --all {{command}} {{command_arguments}}`

- Run a specific command in an existing process's network namespace:

`nsenter --target {{pid}} --net {{command}} {{command_arguments}}`

- Run a specific command in an existing process's PID namespace:

`nsenter --target {{pid}} --pid {{command}} {{command_arguments}}`

- Run a specific command in an existing process's IPC namespace:

`nsenter --target {{pid}} --ipc {{command}} {{command_arguments}}`

- Run a specific command in an existing process's UTS, time, and IPC namespaces:

`nsenter --target {{pid}} --uts --time --ipc -- {{command}} {{command_arguments}}`

- Run a specific command in an existing process's namespace by referencing procfs:

`nsenter --pid=/proc/{{pid}}/pid/net -- {{command}} {{command_arguments}}`
