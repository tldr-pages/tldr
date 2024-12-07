# apt-clone

> Clona/hace copia de seguridad/restaura el estado de un paquete de un sistema basado en Debian.
> Más información: <https://github.com/mvo5/apt-clone>.

- Clona el estado del paquete del sistema actual en un directorio especificado:

`apt-clone clone {{ruta/al/directorio}}`

- Crea un archivo clon (`tar.gz`) con fines de copia de seguridad:

`apt-clone clone --destination {{ruta/a/backup.tar.gz}}`

- Restaura el estado del paquete desde un archivo clon:

`apt-clone restore {{ruta/a/backup.tar.gz}}`

- Muestra información sobre un archivo clon (por ejemplo, la versión, la arquitectura):

`apt-clone info {{ruta/a/backup.tar.gz}}`

- Comprueba si el archivo clon se puede restaurar en el sistema actual:

`apt-clone restore {{ruta/a/backup.tar.gz}} --destination {{ruta/a/restaurar}}`
