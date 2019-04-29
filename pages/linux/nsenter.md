# nsenter

> Run a new command in a running process' namespace.
> Particularly useful for docker images of chroot jails.

- Run command in existing processes network namespace:

`nsenter -t {{pid}} -n {{command}} {{command_arguments}}`

- Run a new command in an existing processes ps-table namespace:

`nsenter -t {{pid}} -p {{command}} {{command_arguments}}`

- Run command in existing processes network namespace:

`nsenter -t {{pid}} -n {{command}} {{command_arguments}}`
