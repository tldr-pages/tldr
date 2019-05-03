# ipcmk

> Create IPC (Inter-process Communication) resources.

- Create shared memory segment:

`ipcmk --shmem {{segment_size_in_bytes}}`

- Create semaphore:

`ipcmk --semaphore {{element_size}}`

- Create message queue:

`ipcmk --queue`

- Create shared memory segment with permissions other than 0644:

`ipcmk --shmem {{segment_size_in_bytes}} {{octal_permissons}}`
