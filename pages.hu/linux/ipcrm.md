# ipcrm

> IPC (Inter-process Communication) erőforrások törlése. További információ: <https://manned.org/ipcrm>.

- Megosztott memóriaszegmens törlése azonosító alapján:

`ipcrm --shmem-id {{shmem_id}}`

- Megosztott memóriaszegmens törlése kulcs szerint:

`ipcrm --shmem-key {{shmem_key}}`

- IPC-várólista törlése azonosító szerint:

`ipcrm --queue-id {{ipc_queue_id}}`

- IPC-várólista törlése kulcs szerint:

`ipcrm --queue-key {{ipc_queue_key}}`

- Szemafor törlése ID szerint:

`ipcrm --semaphore-id {{semaphore_id}}`

- Szemafor törlése kulcs szerint:

`ipcrm --semaphore-key {{semaphore_key}}`

- Az összes IPC-erőforrás törlése:

`ipcrm --all`
