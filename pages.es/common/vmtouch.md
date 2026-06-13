# vmtouch

> Gestiona la caché del sistema de archivos.
> Más información: <https://manned.org/vmtouch>.

- Imprime el estado de la caché de un archivo:

`vmtouch {{ruta/al/archivo}}`

- Carga un archivo en la caché:

`vmtouch -t {{ruta/al/archivo}}`

- Expulsa un archivo de la caché:

`vmtouch -e {{ruta/al/archivo}}`

- Bloquea un archivo en la memoria caché para evitar que salga de la memoria:

`vmtouch -l {{ruta/al/archivo}}`

- Bloquea un archivo y daemoniza el programa:

`vmtouch -ld {{ruta/al/archivo}}`
