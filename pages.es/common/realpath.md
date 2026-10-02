# realpath

> Muestra la ruta absoluta resuelta de un archivo o directorio.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>.

- Muestra la ruta absoluta de un archivo o directorio:

`realpath {{ruta/al/archivo_o_directorio}}`

- Requiere que existan todos los componentes de la ruta:

`realpath {{[-e|--canonicalize-existing]}} {{ruta/al/archivo_o_directorio}}`

- Resuelve los componentes `..` antes que los enlaces simbólicos:

`realpath {{[-L|--logical]}} {{ruta/al/archivo_o_directorio}}`

- Desactiva la expansión de enlaces simbólicos:

`realpath {{[-s|--no-symlinks]}} {{ruta/al/archivo_o_directorio}}`

- Suprime los mensajes de error:

`realpath {{[-q|--quiet]}} {{ruta/al/archivo_o_directorio}}`
