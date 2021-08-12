# ipcmk

> Creați resurse IPC (Comunicare inter-proces).

- Creați un segment de memorie partajată:

`ipcmk --shmem {{segment_size_in_bytes}}`

- Creează un semafor:

`ipcmk --semaphore {{element_size}}`

- Creați o coadă de mesaj:

`ipcmk --queue`

- Creați un segment de memorie partajată cu permisiuni specifice (implicit este 0644):

`ipcmk --shmem {{segment_size_in_bytes}} {{octal_permissons}}`
