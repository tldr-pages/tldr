# asciidoctor

> Un procesador que convierte archivos AsciiDoc a un formato publicable.
> Más información: <https://docs.asciidoctor.org>.

- Convierte un archivo `.adoc` específico a HTML (el formato de salida por defecto):

`asciidoctor {{ruta/al/archivo.adoc}}`

- Convierte un archivo `.adoc` específico a HTML y vincula una hoja de estilos CSS:

`asciidoctor -a stylesheet {{ruta/al/stylesheet.css}} {{ruta/al/archivo.adoc}}`

- Convierte un archivo específico `.adoc` en HTML incrustable, eliminando todo excepto el cuerpo:

`asciidoctor --embedded {{ruta/al/archivo.adoc}}`

- Convierte un archivo `.adoc` dado en un PDF utilizando la biblioteca `asciidoctor-pdf`:

`asciidoctor --backend {{pdf}} --require {{asciidoctor-pdf}} {{ruta/al/archivo.adoc}}`
