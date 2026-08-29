# gawk

> Versión GNU de awk, un lenguaje de programación versátil para trabajar con archivos.
> Vea también: `awk`.
> Más información: <https://www.gnu.org/software/gawk/manual/gawk.html>.

- Imprime la quinta columna (también conocida como campo) de un archivo separado por espacios:

`gawk '{print $5}' {{ruta/al/archivo}}`

- Imprime la segunda columna de las líneas que contengan "foo" en un archivo separado por espacios:

`gawk '/{{foo}}/ {print $2}' {{ruta/al/archivo}}`

- Imprime la última columna de cada línea de un archivo, utilizando una coma (en lugar de un espacio) como separador de campos:

`gawk {{[-F|--field-separator]}} ',' '{print $NF}' {{ruta/al/archivo}}`

- Suma los valores de la primera columna de un archivo e imprime el total:

`gawk '{s+=$1} END {print s}' {{ruta/al/archivo}}`

- Imprime cada tercera línea a partir de la primera:

`gawk 'NR%3==1' {{ruta/al/archivo}}`

- Imprime valores diferentes en función de las condiciones:

`gawk '{if ($1 == "foo") print "Coincidencia exacta con foo"; else if ($1 ~ "bar") print "Coincidencia parcial con bar"; else print "Baz"}' {{ruta/al/archivo}}`

- Imprime todas las líneas en las que el valor de la décima columna esté comprendido entre un mínimo y un máximo:

`gawk '($10 >= {{min_value}} && $10 <= {{max_value}})' {{path/to/file}}`

- Imprime una tabla de usuarios con UID >=1000 con encabezado y salida formateada, utilizando dos puntos como separador (`%-20s` significa: cadena de 20 caracteres alineada a la izquierda; `%6s` significa: cadena de 6 caracteres alineada a la derecha):

`gawk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Nombre", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
