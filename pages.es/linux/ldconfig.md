# ldconfig

> Configura enlaces simbólicos y caché para dependencias de biblioteca compartidas.
> Más información: <https://manned.org/ldconfig>.

- Actualiza los enlaces simbólicos y reconstruye el caché (normalmente se ejecuta cuando se instala una nueva biblioteca):

`sudo ldconfig`

- Actualiza los enlaces simbólicos para un directorio dado:

`sudo ldconfig -n {{ruta/al/directorio}}`

- Imprime las bibliotecas en el caché y comprueba si una biblioteca dada está presente:

`ldconfig -p | grep {{nombre_de_biblioteca}}`
