# tr

> Traduce caracteres: ejecuta sustituciones basadas en caracteres individuales y conjuntos de caracteres.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- Sustituye todas las apariciones de un carácter en un archivo e imprime el resultado:

`tr < {{path/to/file}} {{find_character}} {{replace_character}}`

- Sustituye todas las apariciones de un carácter de la salida de otro comando:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- Mapea cada carácter del primer conjunto al carácter correspondiente del segundo:

`tr < {{path/to/file}} '{{abcd}}' '{{jkmn}}'`

- Elimina todas las apariciones del conjunto de caracteres especificado de la entrada:

`tr < {{path/to/file}} {{[-d|--delete]}} '{{input_characters}}'`

- Comprime una serie de caracteres idénticos a un solo carácter:

`tr < {{path/to/file}} {{[-s|--squeeze-repeats]}} '{{input_characters}}'`

- Traduce el contenido de un archivo a mayúsculas:

`tr < {{path/to/file}} "[:lower:]" "[:upper:]"`

- Elimina los caracteres no imprimibles de un archivo:

`tr < {{path/to/file}} {{[-cd|--complement --delete]}} "[:print:]"`
