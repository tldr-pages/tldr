# nsenter

> Run a new command in a running process' namespace.
> Particularly useful for docker images or chroot jails.
> More information: <https://github.com/jpetazzo/nsenter>.

- Run a command in the network namespace of {{pid}}:

`nsenter --target {{pid}} --net -- {{command}} {{command_arguments}}`

- Run a command in the PID namespace of {{pid}}:

`nsenter --target {{pid}} --pid -- {{command}} {{command_arguments}}`

- Run a command in the UTS, time, and IPC namespace of {{pid}}:

`nsenter --target {{pid}} --uts --time --ipc -- {{command}} {{command_arguments}}`

- Run a command in the network namespace of {{pid}} with the process's procfs namespace directory:

`nsenter --pid=/proc/{{pid}}/pid/net -- {{command}} {{command_arguments}}`
