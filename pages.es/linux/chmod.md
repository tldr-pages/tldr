# chmod

>Cambia los permisos de acceso de un archivo o directorio. Más información: https://www.gnu.org/software/coreutils/chmod.

- Dar al usuario que posee el archivo el permiso de ejecución:

`chmod u+x {{ruta/al/archivo}}`

- Dar al usuario permisos de lectura y escritura al archivo o directorio:

`chmod u+rw {{ruta/al/archivo_o_directorio}}`

- Remover permisos de ejecución para el grupo:

`chmod g-x {{ruta/al/archivo}}`

- Dar a todos los usuarios permisos de lectura y ejecución:

`chmod a+rx {{ruta/al/archivo}}`

- Dar a otros usuarios los mismos permisos que el grupo:

`chmod o=g {{ruta/al/archivo}}`

- Remover todos los permisos de los otros:

`chmod o= {{ruta/al/archivo}}`

- Cambiar los permisos recursivamente dando al grupo y los otros la habilidad de escribir:

`chmod -R g+w,o+w {{ruta/al/directorio}}`

- Recursivamente dar a todos los usuarios permisos de lectura y ejecución de los subdirectorios de un directorio:

`chmod -R a+rX {{ruta/al/directorio}}`
