# apt-file

> Busca archivos en paquetes APT, incluyendo los que aún no fueron instalados.
> Más información: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Actualiza los metadatos de la base de datos:

`sudo apt update`

- Busca paquetes que contengan el archivo o ruta especificada:

`apt-file search {{ruta/al/archivo}}`

- Muestra el contenido del paquete especificado:

`apt-file list {{nombre_paquete}}`
