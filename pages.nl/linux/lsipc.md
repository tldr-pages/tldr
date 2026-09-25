# lsipc

> Toon informatie over System V IPC-faciliteiten die momenteel in gebruik zijn op het systeem.
> Zie ook: `ipcs`.
> Meer informatie: <https://manned.org/lsipc>.

- Toon informatie over alle actieve IPC-faciliteiten:

`lsipc`

- Toon informatie over actieve gedeelde [m]emory-segmenten, berichten[q]ueues of [s]emaphore-sets:

`lsipc {{--shmems|--queues|--semaphores}}`

- Toon volledige details over de resource met een specifieke ID:

`lsipc {{--shmems|--queues|--semaphores}} {{[-i|--id]}} {{resource_id}}`

- Toon de opgegeven outputkolommen (bekijk alle ondersteunde kolommen met `--help`):

`lsipc {{[-o|--output]}} {{KEY,ID,PERMS,SEND,STATUS,NSEMS,RESOURCE,...}}`

- Gebruik het [r]aw, [J]SON, [l]ist, of [e]xport (key="value") formaat:

`lsipc {{--raw|--json|--list|--export}}`

- Kap de output niet af:

`lsipc --notruncate`
