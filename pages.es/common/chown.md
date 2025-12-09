# chown

> Cambia la propiedad de usuario y grupo de archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

- Cambia el usuario propietario de un archivo/directorio:

`chown {{usuario}} {{ruta/al/archivo_o_directorio}}`

- Cambia el usuario y grupo propietario de un archivo/directorio:

`chown {{usuario}}:{{grupo}} {{ruta/al/archivo_o_directorio}}`

- Cambia el usuario propietario y el grupo para que ambos sean `usuario`:

`chown {{usuario}}: {{ruta/al/archivo_o_directorio}}`

- Cambia recursivamente el propietario de un directorio y su contenido:

`chown {{[-R|--recursive]}} {{usuario}} {{ruta/a/directorio}}`

- Cambia el propietario de un enlace simbólico:

`chown {{[-h|--no-dereference]}} {{usuario}} {{ruta/al/enlace_simbólico}}`

- Cambia el propietario de un archivo/directorio para que coincida con un archivo de referencia:

`chown --reference {{ruta/al/archivo_de_referencia}} {{ruta/al/archivo_o_directorio}}`
