# findmnt

> Busca tu sistema de archivos.
> Más información: <https://manned.org/findmnt>.

- Lista todos los sistemas de archivos montados:

`findmnt`

- Busca un dispositivo:

`findmnt {{/dev/sdb1}}`

- Busca un punto de montaje:

`findmnt {{/}}`

- Busca sistemas de archivos de un tipo específico:

`findmnt {{[-t|--types]}} {{ext4,virtiofs,btrfs,...}}`

- Busca sistemas de archivos con una etiqueta específica:

`findmnt LABEL={{BigStorage}}`

- Comprueba en detalle el contenido de la tabla de montaje y verifica `/etc/fstab`:

`findmnt {{[-x|--verify]}} --verbose`
