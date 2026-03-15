# dpkg

> Administrador de paquetes de Debian.
> Algunos subcomandos como `deb` tienen su propia documentación de uso.
> Para comandos equivalentes en otros gestores de paquetes, vea <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Más información: <https://manned.org/dpkg>.

- Instala un paquete:

`sudo dpkg {{[-i|--install]}} {{ruta/al/archivo.deb}}`

- Remueve un paquete:

`sudo dpkg {{[-r|--remove]}} {{paquete}}`

- Lista los paquetes instalados:

`dpkg {{[-l|--list]}} {{patrón}}`

- Lista los contenidos de un paquete:

`dpkg {{[-L|--listfiles]}} {{paquete}}`

- Lista los contenidos de un archivo de paquete local:

`dpkg {{[-c|--contents]}} {{ruta/al/archivo.deb}}`

- Averigua qué paquete posee un archivo:

`dpkg {{[-S|--search]}} {{ruta/al/archivo}}`

- Purga un paquete instalado o ya eliminado, incluyendo su configuración:

`sudo dpkg {{[-P|--purge]}} {{paquete}}`
