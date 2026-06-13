# blahaj

> Un coloreador de salida tipo lolcat que también imprime banderas y tiburones de colores.
> Más información: <https://codeberg.org/GeopJr/BLAHAJ>.

- Obtén una lista de posibles banderas/colores:

`blahaj --flags`

- Imprime un tiburón (blahaj) con colores trans por defecto:

`blahaj {{[-s|--shark]}}`

- Imprime una bandera aleatoria con un multiplicador de tamaño 2x:

`blahaj {{[-f|--flag]}} {{[-r|--random]}} {{[-m|--multiplier]}} 2`

- Imprime el resultado de un comando que produce texto con colores lesbianos:

`{{cowsay "Hola, mundo"}} | blahaj {{[-c|--colors]}} lesbian`

- Imprime texto y color por carácter individual:

`echo "{{Hola, mundo}}" | blahaj {{[-i|--individual]}}`

- Imprime el contenido de un documento de texto, coloreando el fondo en lugar del texto, por palabra:

`blahaj {{[-w|--words]}} {{[-b|--background]}} {{ruta/al/archivo}}`
