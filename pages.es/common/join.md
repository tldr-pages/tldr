# join

> Une las líneas de dos archivos ordenados en un campo común.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/join-invocation.html>.

- Une dos archivos en el primer campo (por defecto):

`join {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Une dos archivos utilizando una coma (en lugar de un espacio) como separador de campos:

`join -t {{“,”}} {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Une el campo3 del archivo1 con el campo1 del archivo2:

`join -1 {{3}} -2 {{1}} {{ruta/al/fichero1}} {{ruta/al/archivo2}}`

- Produce una línea por cada línea no emparejable del fichero1:

`join -a {{1}} {{ruta/al/fichero1}} {{ruta/al/archivo2}}`

- Une un fichero desde `stdin`:

`cat {{ruta/al/archivo1}} | join - {{ruta/al/archivo2}}`
