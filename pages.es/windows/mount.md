# mount

> Monta recursos compartidos de red del sistema de archivos de red (NFS).
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/mount>.

- Monta un recurso compartido en la letra de unidad "Z":

`mount \\{{nombre_computadora}}\{{nombre_recurso_compartido}} {{Z:}}`

- Monta un recurso compartido en la siguiente letra de unidad disponible:

`mount \\{{nombre_computadora}}\{{nombre_recurso_compartido}} *`

- Monta un recurso compartido con un tiempo de espera de lectura en segundos (por defecto es 0.8, puede ser de 0.9 a 1 a 60):

`mount -o timeout={{segundos}} \\{{nombre_computadora}}\{{nombre_recurso_compartido}} {{Z:}}`

- Monta un recurso compartido y reintenta hasta 10 veces si falla:

`mount -o retry=10 \\{{nombre_computadora}}\{{nombre_recurso_compartido}} {{Z:}}`

- Monta un recurso compartido con sensibilidad a mayúsculas forzada:

`mount -o casesensitive \\{{nombre_computadora}}\{{nombre_recurso_compartido}} {{Z:}}`

- Monta un recurso compartido como un usuario anónimo:

`mount -o anon \\{{nombre_computadora}}\{{nombre_recurso_compartido}} {{Z:}}`

- Monta un recurso compartido utilizando un tipo de montaje específico:

`mount -o mtype={{soft|hard}} \\{{nombre_computadora}}\{{nombre_recurso_compartido}} {{Z:}}`
