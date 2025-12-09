# lsipc

> Show information on System V IPC facilities currently employed in the system.
> See also: `ipcs` for the older tool.
> More information: <https://manned.org/lsipc>.

- Show information about all active IPC facilities:

`lsipc`

- Show information about active shared [m]emory segments, message [q]ueues or [s]empahore sets:

`lsipc {{--shmems|--queues|--semaphores}}`

- Show full details on the resource with a specific ID:

`lsipc {{--shmems|--queues|--semaphores}} {{[-i|--id]}} {{resource_id}}`

- Print the given output columns (see all supported columns with `--help`):

`lsipc {{[-o|--output]}} {{KEY,ID,PERMS,SEND,STATUS,NSEMS,RESOURCE,...}}`

- Use [r]aw, [J]SON, [l]ist or [e]xport (key="value") format:

`lsipc {{--raw|--json|--list|--export}}`

- Don't truncate the output:

`lsipc --notruncate`
