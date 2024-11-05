# apt-file

> Busca archivos en paquetes `apt`, incluyendo los que aún no han sido instalados.
> Más información: <https://manned.org/apt-file.1>.

- Actualiza los metadatos de la base de datos:

`sudo apt update`

- Busca paquetes que contengan el archivo o ruta especificada:

`apt-file {{search|find}} {{ruta/al/archivo}}`

- Muestra el contenido del paquete especificado:

`apt-file {{show|list}} {{nombre_paquete}}`

- Busca paquetes que coincidan con la `expresión_regular`:

`apt-file {{search|find}} --regexp {{expresión_regular}}`
