# ipcmk

> Maak IPC-resources (Inter-process Communication) aan.
> Meer informatie: <https://manned.org/ipcmk>.

- Maak een gedeeld geheugensegment aan:

`ipcmk {{[-M|--shmem]}} {{segment_size_in_bytes}}`

- Maak een semafoor aan:

`ipcmk {{[-S|--semaphore]}} {{element_size}}`

- Maak een berichtenwachtrij aan:

`ipcmk {{[-Q|--queue]}}`

- Maak een gedeeld geheugensegment aan met specifieke permissies (standaard is 0644):

`ipcmk {{[-M|--shmem]}} {{segment_size_in_bytes}} {{octal_permissions}}`
