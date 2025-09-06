# ipcrm

> Delete IPC (Inter-process Communication) resources.
> More information: <https://manned.org/ipcrm>.

- Delete a shared memory segment by ID:

`ipcrm {{[-m|--shmem-id]}} {{shmem_id}}`

- Delete a shared memory segment by key:

`ipcrm {{[-M|--shmem-key]}} {{shmem_key}}`

- Delete an IPC queue by ID:

`ipcrm {{[-q|--queue-id]}} {{ipc_queue_id}}`

- Delete an IPC queue by key:

`ipcrm {{[-Q|--queue-key]}} {{ipc_queue_key}}`

- Delete a semaphore by ID:

`ipcrm {{[-s|--semaphore-id]}} {{semaphore_id}}`

- Delete a semaphore by key:

`ipcrm {{[-S|--semaphore-key]}} {{semaphore_key}}`

- Delete all IPC resources:

`ipcrm {{[-a|--all]}}`
