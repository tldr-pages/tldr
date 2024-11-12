# mount.cifs

> Monta SMB (Server Message Block) o CIFS (Common Internet File System).
> Nota: también puede hacer lo mismo pasando la opción `-t cifs` a `mount`.
> Más información: <https://manned.org/mount.cifs>.

- Conecta el nombre de usuario especificado o `$USER` por defecto (se le pedirá una contraseña):

`mount.cifs -o user={{usuario}} //{{servidor}}/{{nombre_del_share}} {{punto_de_montaje}}`

- Conecta como usuario invitado (sin contraseña):

`mount.cifs -o guest //{{servidor}}/{{nombre_del_share}} {{punto_de_montaje}}`

- Establece información de propiedad para el directorio montado:

`mount.cifs -o uid={{id_del_usuario|usuario}},gid={{id_del_grupo|nombre_del_grupo}} //{{servidor}}/{{nombre_del_share}} {{punto_de_montaje}}`
