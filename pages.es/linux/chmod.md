# chmod

> Cambia los permisos de un archivo o directorio.
> Más información: <https://manned.org/chmod>.

- Cambia los permisos de un archivo o directorio. Los permisos se pueden especificar en octal o en notación simbólica:

- Octal:

`chmod {{777}} {{ruta/al/archivo}}`

- Simbólica:

`chmod {{u=rwx,g=r,o=r}} {{ruta/al/archivo}}`

- Cambia los permisos de un archivo o directorio recursivamente:

`chmod -R {{777}} {{ruta/al/archivo}}`
