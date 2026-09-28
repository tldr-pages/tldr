# ipcrm

> Verwijder IPC-resources (Inter-process Communication).
> Meer informatie: <https://manned.org/ipcrm>.

- Verwijder een gedeeld geheugensegment op basis van ID:

`ipcrm {{[-m|--shmem-id]}} {{shmem_id}}`

- Verwijder een gedeeld geheugensegment op basis van key:

`ipcrm {{[-M|--shmem-key]}} {{shmem_key}}`

- Verwijder een IPC-wachtrij op basis van ID:

`ipcrm {{[-q|--queue-id]}} {{ipc_queue_id}}`

- Verwijder een IPC-wachtrij op basis van key:

`ipcrm {{[-Q|--queue-key]}} {{ipc_queue_key}}`

- Verwijder een semafoor op basis van ID:

`ipcrm {{[-s|--semaphore-id]}} {{semaphore_id}}`

- Verwijder een semafoor op basis van key:

`ipcrm {{[-S|--semaphore-key]}} {{semaphore_key}}`

- Verwijder alle IPC-resources:

`ipcrm {{[-a|--all]}}`
