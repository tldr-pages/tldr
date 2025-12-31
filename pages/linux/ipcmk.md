# ipcmk

> Create IPC (Inter-process Communication) resources.
> More information: <https://manned.org/ipcmk>.

- Create a shared memory segment:

`ipcmk {{[-M|--shmem]}} {{segment_size_in_bytes}}`

- Create a semaphore:

`ipcmk {{[-S|--semaphore]}} {{element_size}}`

- Create a message queue:

`ipcmk {{[-Q|--queue]}}`

- Create a shared memory segment with specific permissions (default is 0644):

`ipcmk {{[-M|--shmem]}} {{segment_size_in_bytes}} {{octal_permissions}}`
