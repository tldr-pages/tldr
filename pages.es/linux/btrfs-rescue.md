# btrfs rescue

> Intenta recuperar un sistema de archivos btrfs dañado.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- Reconstruye el árbol de metadatos del sistema de archivos (muy lento):

`sudo btrfs rescue chunk-recover {{ruta/a/la_partición}}`

- Corrige problemas relacionados con la alineación del tamaño del dispositivo (por ejemplo, incapacidad para montar el sistema de archivos debido a una discrepancia en los bytes totales del superbloque):

`sudo btrfs rescue fix-device-size {{ruta/a/la_partición}}`

- Recupera un superbloque dañado de copias correctas (recupera la raíz del árbol de archivos del sistema):

`sudo btrfs rescue super-recover {{ruta/a/la_partición}}`

- Recupera de transacciones interrumpidas (corrige problemas de reproducción de registros):

`sudo btrfs rescue zero-log {{ruta/a/la_partición}}`

- Crea un dispositivo de control `/dev/btrfs-control` cuando `mknod` no está instalado:

`sudo btrfs rescue create-control-device`
