# autoflake

> Herramienta para eliminar importaciones y variables no utilizadas en archivos Python.
> Más información: <https://github.com/myint/autoflake>.

- Elimina variables no utilizadas de un único archivo y muestra las diferencias:

`autoflake --remove-unused-variables {{ruta/al/archivo.py}}`

- Elimina importaciones no utilizadas de varios archivos y muestra las diferencias de cada uno de ellos:

`autoflake --remove-all-unused-imports {{ruta/al/archivo1.py ruta/al/archivo2.py ...}}`

- Elimina variables no utilizadas de un archivo, sobrescribiendo el mismo:

`autoflake --remove-unused-variables --in-place {{ruta/al/archivo.py}}`

- Elimina variables no utilizadas recursivamente de todos los archivos en un directorio, sobrescribiendo cada uno de ellos:

`autoflake --remove-unused-variables --in-place --recursive {{ruta/al/directorio}}`
