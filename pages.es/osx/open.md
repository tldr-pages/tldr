# open

> Abre archivos, directorios y aplicaciones.
> Más información: <https://keith.github.io/xcode-man-pages/open.1.html>.

- Abre un archivo con la aplicación asociada:

`open {{archivo.ext}}`

- Ejecuta una [a]plicación gráfica de macOS:

`open -a "{{aplicacion}}"`

- Ejecuta una aplicación gráfica de macOS basada en el identificador [b]undle (consulta `osascript` para obtenerlo fácilmente):

`open -b {{com.domain.application}}`

- Abre el directorio actual en Finder:

`open .`

- Abre un archivo en Finder:

`open -R {{ruta/al/archivo}}`

- Abre todos los archivos de una extensión determinada en el directorio actual con la aplicación asociada:

`open {{*.ext}}`

- Abre una [n]ueva instancia de una aplicación especificada mediante un identificador [b]undle:

`open -n -b {{com.domain.application}}`
