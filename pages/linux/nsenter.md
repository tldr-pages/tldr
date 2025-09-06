# nsenter

> Run a new command in a running process' namespace.
> Particularly useful for Docker images or chroot jails.
> More information: <https://manned.org/nsenter>.

- Run a specific command using the same namespaces as an existing process:

`nsenter {{[-t|--target]}} {{pid}} {{[-a|--all]}} {{command}} {{command_arguments}}`

- Run a specific command in an existing process's mount|UTS|IPC|network|PID|user|cgroup|time namespace:

`nsenter {{[-t|--target]}} {{pid}} --{{mount|uts|ipc|net|pid|user|cgroup}} {{command}} {{command_arguments}}`

- Run a specific command in an existing process's UTS, time, and IPC namespaces:

`nsenter {{[-t|--target]}} {{pid}} {{[-u|--uts]}} {{[-T|--time]}} {{[-i|--ipc]}} -- {{command}} {{command_arguments}}`

- Run a specific command in an existing process's namespace by referencing procfs:

`nsenter {{[-p|--pid=]}}/proc/{{pid}}/pid/net -- {{command}} {{command_arguments}}`
