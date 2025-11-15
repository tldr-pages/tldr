# dpkg-deb

> Empaqueta, desempaqueta y proporciona información sobre archivos Debian.
> Más información: <https://manned.org/dpkg-deb>.

- Muestra información sobre un paquete:

`dpkg-deb --info {{ruta/al/archivo.deb}}`

- Muestra el nombre y la versión del paquete en una línea:

`dpkg-deb --show {{ruta/al/archivo.deb}}`

- Lista el contenido del paquete:

`dpkg-deb --contents {{ruta/al/archivo.deb}}`

- Extrae el contenido del paquete en un directorio:

`dpkg-deb --extract {{ruta/al/archivo.deb}} {{ruta/al/directorio}}`

- Crea un paquete desde un directorio especificado:

`dpkg-deb --build {{ruta/al/directorio}}`
