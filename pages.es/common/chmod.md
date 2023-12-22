# chmod

> Cambia los permisos de acceso de un archivo o directorio.
> Más información: <https://www.gnu.org/software/coreutils/chmod>.

- Otorga al [u]suario que es propietario del archivo permiso para [x] ejecutarlo:

`chmod u+x {{ruta/al/archivo}}`

- Otorga al [u]suario derechos para leer (r) y escribir (w) un archivo o directorio:

`chmod u+rw {{ruta/al/archivo_o_directorio}}`

- Elimina los derechos de ejecución del [g]rupo:

`chmod g-x {{ruta/al/archivo}}`

- Otorga a todos los usuarios (a) derechos para leer y ejecutar:

`chmod a+rx {{ruta/al/archivo}}`

- Otorga a [o]tros (que no están en el grupo del propietario) los mismos derechos que los del [g]rupo:

`chmod o=g {{ruta/al/archivo}}`

- Quitar todos los derechos a [o]tros:

`chmod o= {{ruta/al/archivo}}`

- Otorga al [g]rupo y a [o]tros el derecho para escribir (w) un directorio y su contenido:

`chmod -R g+w,o+w {{ruta/al/directorio}}`

- Concede de forma recursiva [a] todos los usuarios permisos de lectu[r]a a los archivos y permisos de e[X]ecución a los subdirectorios dentro de un directorio:

`chmod -R a+rX {{ruta/al/directorio}}`
