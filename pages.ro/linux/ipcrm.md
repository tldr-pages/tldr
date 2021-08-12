# ipcrm

> Ștergeți resursele IPC (Comunicare inter-proces).

- Ștergeți un segment de memorie partajată după ID:

`ipcrm --shmem-id {{shmem_id}}`

- Ștergeți un segment de memorie partajată după cheie:

`ipcrm --shmem-key {{shmem_key}}`

- Ștergeți o coadă IPC după ID:

`ipcrm --queue-id {{ipc_queue_id}}`

- Ștergeți o coadă IPC după cheie:

`ipcrm --queue-key {{ipc_queue_key}}`

- Ștergeți un semafor prin ID:

`ipcrm --semaphore-id {{semaphore_id}}`

- Ștergeți un semafor cu cheie:

`ipcrm --semaphore-key {{semaphore_key}}`

- Ștergeți toate resursele IPC:

`ipcrm --all`
