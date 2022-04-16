# nsenter

> Run a new command in a running process' namespace.
> Particularly useful for docker images or chroot jails.
> More information: <https://manned.org/nsenter>.

- Run command using all the same namespaces as an existing process:

`nsenter --target {{pid}} --all {{command}} {{command_arguments}}`

- Run command in an existing process's network namespace:

`nsenter --target {{pid}} --net {{command}} {{command_arguments}}`

- Run command in an existing process's PID namespace:

`nsenter --target {{pid}} --pid {{command}} {{command_arguments}}`

- Run command in an existing process's IPC namespace:

`nsenter -t {{pid}} -i {{command}} {{command_arguments}}`
