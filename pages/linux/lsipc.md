# lsipc

> Show information on System V IPC facilities currently employed in the system.
> See also: `ipcs` for the older tool.
> More information: <https://manned.org/lsipc>.

- Show information about all active IPC facilities:

`lsipc`

- Show information about active shared [m]emory segments, message [q]ueues or [s]empahore sets:

`lsipc {{--shmems|--queues|--semaphores}}`

- Show full details on the resource with a specific [i]D:

`lsipc {{--shmems|--queues|--semaphores}} --id {{resource_id}}`

- Print the given [o]utput columns (see all supported columns with `--help`):

`lsipc --output {{KEY,ID,PERMS,SEND,STATUS,NSEMS,RESOURCE,...}}`

- Use [r]aw, [J]SON, [l]ist or [e]xport (key="value") format:

`lsipc {{--raw|--json|--list|--export}}`

- Don't truncate the output:

`lsipc --notruncate`
