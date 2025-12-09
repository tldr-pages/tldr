# apt-cache

> Herramienta de consulta de paquetes para Debian y Ubuntu.
> Más información: <https://manned.org/apt-cache.8>.

- Busca un paquete en tus fuentes actuales:

`apt-cache search {{consulta}}`

- Muestra información de un paquete:

`apt-cache show {{paquete}}`

- Muestra si un paquete está instalado y actualizado:

`apt-cache policy {{paquete}}`

- Muestra las dependencias de un paquete:

`apt-cache depends {{paquete}}`

- Muestra los paquetes que dependen de un paquete en particular:

`apt-cache rdepends {{paquete}}`
