# tr

> Traduce caracteres: ejecuta sustituciones basadas en caracteres individuales y conjuntos de caracteres.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- Sustituye todas las apariciones de un carácter en un archivo e imprime el resultado:

`tr {{carácter_a_buscar}} {{carácter_a_sustituir}} < {{ruta/al/archivo}}`

- Sustituye todas las apariciones de un carácter de la salida de otro comando:

`echo {{texto}} | tr {{carácter_a_buscar}} {{carácter_a_sustituir}}`

- Mapea cada carácter del primer conjunto al carácter correspondiente del segundo:

`tr '{{abcd}}' '{{jkmn}}' < {{ruta/al/archivo}}`

- Elimina todas las apariciones del conjunto de caracteres especificado de la entrada:

`tr -d '{{caracteres_de_entrada}}' < {{ruta/al/archivo}}`

- Comprime una serie de caracteres idénticos a un solo carácter:

`tr -s '{{caracteres_de_entrada}}' < {{ruta/al/archivo}}`

- Traduce el contenido de un archivo a mayúsculas:

`tr "[:lower:]" "[:upper:]" < {{ruta/al/archivo}}`

- Elimina los caracteres no imprimibles de un archivo:

`tr -cd "[:print:]" < {{ruta/al/archivo}}`
