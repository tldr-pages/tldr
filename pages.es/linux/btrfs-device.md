# btrfs device

> Gestiona dispositivos en un sistema de archivos btrfs.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Agrega uno o más dispositivos a un sistema de archivos btrfs:

`sudo btrfs {{[d|device]}} {{[a|add]}} {{ruta/al/dispositivo_bloque1 ruta/al/dispositivo_bloque2 ...}} {{ruta/al_sistema_de_archivos_btrfs}}`

- Elimina un dispositivo de un sistema de archivos btrfs:

`sudo btrfs {{[d|device]}} {{[rem|remove]}} {{ruta/al/dispositivo|id_del_dispositivo}}`

- Muestra estadísticas de errores:

`sudo btrfs {{[d|device]}} {{[st|stats]}} {{ruta/al_sistema_de_archivos_btrfs}}`

- Escanea todos los discos e informa al kernel de todos los sistemas de archivos btrfs detectados:

`sudo btrfs {{[d|device]}} {{[sc|scan]}} {{[-d|--all-devices]}}`

- Muestra estadísticas detalladas de asignación por disco:

`sudo btrfs {{[d|device]}} {{[u|usage]}} {{ruta/al_sistema_de_archivos_btrfs}}`
