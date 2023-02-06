# ipcmk

> IPC (Inter-process Communication) erőforrások létrehozása. További információ: <https://manned.org/ipcmk>.

- Hozzon létre egy megosztott memória szegmenst:

`ipcmk --shmem {{segment_size_in_bytes}}`

- Szemafor létrehozása:

`ipcmk --semaphore {{element_size}}`

- Üzenetváró sor létrehozása:

`ipcmk --queue`

- Megosztott memóriaszegmens létrehozása meghatározott jogosultságokkal (alapértelmezett 0644):

`ipcmk --shmem {{segment_size_in_bytes}} {{octal_permissions}}`
