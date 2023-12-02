# chmod

> Cambia los permisos de acceso de un archivo o directorio.
> Más información: <https://www.gnu.org/software/coreutils/chmod>.

- Otorga al [u]suario que es propietario del archivo permiso para [x] ejecutarlo:

`chmod u+x {{ruta/al/archivo}}`

- Otorga al usuario derechos para leer (r) y escribir (w) un archivo o directorio:

`chmod u+rw {{ruta/al/archivo_o_directorio}}`

- Elimina los derechos de ejecución del [g]rupo:

`chmod g-x {{ruta/al/archivo}}`

- Otorga a todos los usuarios (a) derechos para leer y ejecutar:

`chmod a+rx {{ruta/al/archivo}}`

- Otorga a [o]tros (que no están en el grupo del propietario) los mismos derechos que los del grupo:

`chmod o=g {{ruta/al/archivo}}`

- Remove all rights from [o]thers:

`chmod o= {{ruta/al/archivo}}`

- Otorga al [g]rupo y a [o]tros el derecho para escribir (w) un directorio y su contenido:

`chmod -R g+w,o+w {{ruta/al/directorio}}`

- Recursively give [a]ll users [r]ead permissions to files and e[X]ecute permissions to sub-directories within a directory:

`chmod -R a+rX {{ruta/al/directorio}}`
