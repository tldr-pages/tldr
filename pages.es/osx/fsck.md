# fsck

> Comprueba la integridad de un sistema de archivos o los repara. El sistema de ficheros debe estar desmontado en el momento de ejecutar el comando.
> Es una envoltura que llama a `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, y `fsck_udf` según sea necesario.
> Más información: <https://ss64.com/osx/fsck.html>.

- Comprueba el sistema de ficheros `/dev/sdX`, informando de cualquier bloque dañado:

`fsck {{/dev/sdX}}`

- Comprueba el sistema de ficheros `/dev/sdX` sólo si está limpio, informando de los bloques dañados y dejando que el usuario elija interactivamente si repara cada uno de ellos:

`fsck -f {{/dev/sdX}}`

- Comprueba el sistema de archivos `/dev/sdX` sólo si está limpio, informando de los bloques dañados y reparándolos automáticamente:

`fsck -fy {{/dev/sdX}}`

- Comprueba el sistema de archivos `/dev/sdX`, informando si se ha desmontado correctamente:

`fsck -q {{/dev/sdX}}`
