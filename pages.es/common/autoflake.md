# autoflake

> Una herramienta para eliminar importaciones y variables no utilizadas del código Python.
> Más información: <https://github.com/myint/autoflake>.

- Elimina las variables no utilizadas de un único archivo y muestra la diferencia:

`autoflake --remove-unused-variables {{archivo.py}}`

- Elimina las importaciones no utilizadas de varios archivos y muestra las diferencias:

`autoflake --remove-all-unused-imports {{archivo1.py}} {{archivo2.py}} {{archivo3.py}}`

- Elimina variables no utilizadas de un archivo, sobrescribiendo el archivo:

`autoflake --remove-unused-variables --in-place {{archivo.py}}`

- Elimina las variables no utilizadas recursivamente de todos los archivos en un directorio, sobrescribiendo cada archivo:

`autoflake --remove-unused-variables --in-place --recursive {{ruta/al/directorio}}`
