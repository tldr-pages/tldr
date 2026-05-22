# mkisofs

> Crea archivos ISO a partir de directorios.
> También conocido como `genisoimage`.
> Más información: <https://manned.org/mkisofs>.

- Crea un ISO a partir de un directorio:

`mkisofs -o {{nombre_archivo.iso}} {{ruta/al/directorio_de_origen}}`

- Establece la etiqueta del disco al crear una ISO:

`mkisofs -o {{nombre_archivo.iso}} -V "{{nombre_etiqueta}}" {{ruta/al/directorio_de_origen}}`

- Crea una imagen ISO con archivos de más de 2 GiB indicando un tamaño aparente menor para sistemas de archivos ISO9660:

`mkisofs -o {{nombre_archivo.iso}} -allow-limited-size {{ruta/al/directorio_de_origen}}`
