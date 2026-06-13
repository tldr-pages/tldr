# share

> Hace que el recurso/sistema de archivos local esté disponible para ser montado por sistemas remotos.
> Más información: <https://docs.oracle.com/cd/E36784_01/html/E36825/gntjt.html>.

- Lista todos los sistemas de archivos compartidos actualmente:

`share`

- Comparte un directorio con acceso de lectura/escritura:

`share -F nfs -o rw {{/ruta/al/directorio}}`

- Comparte un directorio con acceso de solo lectura:

`share -F nfs -o ro {{/ruta/al/directorio}}`

- Comparte un directorio con opciones específicas (por ejemplo, permitir el acceso root desde un host concreto):

`share -F nfs -o rw,root={{nombre_del_host}} {{/ruta/al/directorio}}`

- Hace que la compartición sea persistente añadiendo entradas a `/etc/dfs/dfstab`:

`echo "share -F nfs -o rw {{/ruta/al/directorio}}" >> /etc/dfs/dfstab`
