# asciiart

> Convierte imágenes en ASCII.
> Más información: <https://github.com/nodanaonlyzuul/asciiart>.

- Lee una imagen de un archivo y la muestra en ASCII:

`asciiart {{ruta/a/la/imagen.jpg}}`

- Lee una imagen desde una URL y la muestra en ASCII:

`asciiart {{www.example.com/image.jpg}}`

- Elige el ancho de salida (por defecto es 100):

`asciiart --width {{50}} {{ruta/a/la/imagen.jpg}}`

- Coloriza la salida ASCII:

`asciiart --color {{ruta/a/la/imagen.jpg}}`

- Elige el formato de salida (formato predeterminado es texto):

`asciiart --format {{text|html}} {{ruta/a/la/imagen.jpg}}`

- Invierte el mapa de caracteres:

`asciiart --invert-chars {{ruta/a/la/imagen.jpg}}`
