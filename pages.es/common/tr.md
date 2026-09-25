# tr

> Traduce caracteres: ejecuta sustituciones basadas en caracteres individuales y conjuntos de caracteres.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- Sustituye todas las apariciones de un carácter en un archivo e imprime el resultado:

`tr < {{ruta/al/archivo}} {{find_character}} {{replace_character}}`

- Sustituye todas las apariciones de un carácter de la salida de otro comando:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- Mapea cada carácter del primer conjunto al carácter correspondiente del segundo:

`tr < {{ruta/al/archivo}} '{{abcd}}' '{{jkmn}}'`

- Elimina todas las apariciones del conjunto de caracteres especificado de la entrada:

`tr < {{ruta/al/archivo}} {{[-d|--delete]}} '{{input_characters}}'`

- Comprime una serie de caracteres idénticos a un solo carácter:

`tr < {{ruta/al/archivo}} {{[-s|--squeeze-repeats]}} '{{input_characters}}'`

- Traduce el contenido de un archivo a mayúsculas:

`tr < {{ruta/al/archivo}} "[:lower:]" "[:upper:]"`

- Elimina los caracteres no imprimibles de un archivo:

`tr < {{ruta/al/archivo}} {{[-cd|--complement --delete]}} "[:print:]"`
