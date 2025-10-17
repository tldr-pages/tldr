# chgrp

> Cambia la propiedad de grupo de archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html>.

- Cambia el grupo propietario de un archivo/directorio:

`chgrp {{grupo}} {{ruta/al/archivo_o_directorio}}`

- Cambia recursivamente el grupo propietario de un directorio y su contenido:

`chgrp {{[-R|--recursive]}} {{grupo}} {{ruta/al/directorio}}`

- Cambia el grupo propietario de un enlace simbólico:

`chgrp {{[-h|--no-dereference]}} {{grupo}} {{ruta/al/symlink}}`

- Cambia el grupo propietario de un archivo/directorio para que coincida con un archivo de referencia:

`chgrp --reference {{ruta/al/archivo_de_referencia}} {{ruta/al/archivo_o_directorio}}`
