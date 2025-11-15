# autoflake

> Una herramienta para eliminar importaciones y variables no utilizadas del código Python.
> Más información: <https://github.com/myint/autoflake>.

- Elimina las variables no utilizadas de un archivo y muestra la diferencia:

`autoflake --remove-unused-variables {{ruta/al/archivo.py}}`

- Elimina las importaciones no utilizadas de varios archivos y muestra las diferencias:

`autoflake --remove-all-unused-imports {{ruta/al/archivo1.py ruta/al/archivo2.py ...}}`

- Elimina variables no utilizadas de un fichero, sobrescribiendo el fichero:

`autoflake --remove-unused-variables --in-place {{ruta/al/archivo.py}}`

- Elimina recursivamente las variables no utilizadas de todos los archivos de un directorio, sobrescribiendo cada archivo:

`autoflake --remove-unused-variables --in-place --recursive {{ruta/al/directorio}}`
