# awk

> Un versátil lenguaje de programación para trabajar con archivos.
> Más información: <https://github.com/onetrueawk/awk>.

- Imprime la quinta columna (también conocida como campo) de un archivo separado por espacios:

`awk '{print $5}' {{ruta/al/archivo}}`

- Imprime la segunda columna de las líneas que contienen "foo" en un archivo separado por espacios:

`awk '/{{foo}}/ {print $2}' {{ruta/al/archivo}}`

- Imprime la última columna de cada línea de un archivo, utilizando una coma (en lugar de un espacio) como separador de campos:

`awk -F ',' '{print $NF}' {{ruta/al/archivo}}`

- Suma los valores de la primera columna de un fichero e imprime el total:

`awk '{s+=$1} END {print s}' {{ruta/al/archivo}}`

- Imprime una de cada tres líneas a partir de la primera:

`awk 'NR%3==1' {{ruta/al/archivo}}`

- Imprime diferentes valores basados en condiciones:

`awk '{if ($1 == "foo") print "Coincidencia exacta foo"; else if ($1 ~ "bar") print "Coincidencia parcial bar"; else print "Baz"}' {{ruta/al/archivo}}`

- Imprime todas las líneas en las que el valor de la 10ª columna sea igual al valor especificado:

`awk '($10 == valor)'`

- Imprime todas las líneas en las que el valor de la 10ª columna esté entre un mínimo y un máximo:

`awk '($10 >= valor_mín && $10 <= valor_máx)'`
