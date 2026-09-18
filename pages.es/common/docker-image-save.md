# docker image save

> Exporta imágenes de Docker a un archivo.
> Más información: <https://docs.docker.com/reference/cli/docker/image/save/>.

- Guarda una imagen redirigiendo `stdout` a un archivo `.tar`:

`docker {{[save|image save]}} {{imagen}}:{{etiqueta}} > {{ruta/a/archivo.tar}}`

- Guarda una imagen en un archivo `.tar`:

`docker {{[save|image save]}} {{[-o|--output]}} {{ruta/al/archivo.tar}} {{imagen}}:{{etiqueta}}`

- Guarda todas las etiquetas de la imagen:

`docker {{[save|image save]}} {{[-o|--output]}} {{ruta/al/archivo.tar}} {{nombre_de_la_imagen}}`

- Selecciona etiquetas concretas de una imagen para guardarlas:

`docker {{[save|image save]}} {{[-o|--output]}} {{ruta/al/archivo.tar}} {{nombre_de_la_imagen:etiqueta1 nombre_de_la_imagen:etiqueta2 ...}}`
