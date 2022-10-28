# chmod

> Cambia los permisos de acceso de un archivo o directorio.
> Más información: https://www.gnu.org/software/coreutils/chmod.

- Da al [u]suario que posee al archivo el permiso de ejecución [x]:

`chmod u+x {{ruta/al/archivo}}`

- Da al [u]suario permisos de lectu[r]a y escritura [w] a un archivo o directorio:

`chmod u+rw {{ruta/al/archivo_o_directorio}}`

- Remueve permisos de ejecución [x] del [g]rupo:

`chmod g-x {{ruta/al/archivo}}`

- Da a todos [a] los usuarios permisos de lectu[r]a y ejecución [x]:

`chmod a+rx {{ruta/al/archivo}}`

- Da a [o]tros usuarios (no dentro del grupo dueño del archivo) los mismos permisos que el [g]rupo:

`chmod o=g {{ruta/al/archivo}}`

- Remueve todos los permisos de [o]tros:

`chmod o= {{ruta/al/archivo}}`

- Cambia los permisos recursivamente dando al [g]rupo y a [o]tros la habilidad de escribir [w]:

`chmod -R g+w,o+w {{ruta/al/directorio}}`

- Recursivamente da a todos [a] los usuarios permisos de lectu[r]a y ejecución [X] de los subdirectorios de un directorio:

`chmod -R a+rX {{ruta/al/directorio}}`
