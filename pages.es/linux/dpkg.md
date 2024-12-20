# dpkg

> Administrador de paquetes de Debian.
> Algunos subcomandos como `deb` tienen su propia documentación de uso.
> Para comandos equivalentes en otros gestores de paquetes, vea <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Más información: <https://manned.org/dpkg>.

- Instala un paquete:

`dpkg -i {{ruta/al/archivo.deb}}`

- Remueve un paquete:

`dpkg -r {{paquete}}`

- Lista los paquetes instalados:

`dpkg -l {{patrón}}`

- Lista los contenidos de un paquete:

`dpkg -L {{paquete}}`

- Lista los contenidos de un archivo de paquete local:

`dpkg -c {{ruta/al/archivo.deb}}`

- Averigua qué paquete posee un archivo:

`dpkg -S {{ruta/al/archivo}}`

- Purga un paquete instalado o ya eliminado, incluyendo su configuración:

`dpkg -P {{paquete}}`
