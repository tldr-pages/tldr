# chown

> Cambia la propiedad de usuario y grupo sobre archivos y directorios.

- Cambia el usuario propietario de un archivo/directorio:

`chown {{usuario}} {{ruta/hacia/archivo_o_directorio}}`

- Cambia el usuario y grupo propietario de un archivo/directorio:

`chown {{usuario}}:{{grupo}} {{ruta/hacia/archivo_o_directorio}}`

- Cambia de forma recursiva el propietario sobre un directorio y su contenido:

`chown -R {{usuario}} {{ruta/hacia/directorio}}`

- Cambia el propietario de un enlace simbólico:

`chown -h {{usuario}} {{ruta/hacia/enlace_simbolico}}`

- Copia la información de propiedad del archivo/directorio de referencia a otro:

`chown --reference={{ruta/hacia/archivo_o_directorio_de_referencia}} {{ruta/hacia/archivo_o_directorio}}`
