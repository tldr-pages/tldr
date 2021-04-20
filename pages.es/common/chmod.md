# chmod

> Cambiar los permisos de acceso de un archivo o directorio.
> Más información: <https://www.gnu.org/software/coreutils/chmod>.

- Otorga al [u]suario que es propietario del archivo permiso para [x] ejecutarlo:

`chmod u+x {{archivo}}`

- Otorga al usuario derechos para leer (r) y escribir (w) un archivo o directorio:

`chmod u+rw {{archivo_o_directorio}}`

- Elimina los derechos de ejecución del [g]rupo:

`chmod g-x {{archivo}}`

- Otorga a todos los usuarios (a) derechos para leer y ejecutar:

`chmod a+rx {{archivo}}`

- Otorga a [o]tros (que no están en el grupo del propietario) los mismos derechos que los del grupo:

`chmod o=g {{archivo}}`

- Otorga al [g]rupo y a [o]tros el derecho para escribir (w) un directorio y su contenido:

`chmod -R g+w,o+w {{directorio}}`
