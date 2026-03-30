# wget

> Descarga archivos de la web.
> Admite HTTP, HTTPS y FTP.
> Ver también: `wcurl`, `curl`.
> Más información: <https://www.gnu.org/software/wget/manual/wget.html>.

- Descarga el contenido de una URL en un archivo (llamado "foo" en este caso):

`wget {{https://example.com/foo}}`

- Descarga el contenido de una URL en un archivo con un nombre específico (llamado "bar"):

`wget {{[-O|--output-document]}} {{bar}} {{https://example.com/foo}}`

- Descarga una página web completa con todos sus recursos con intervalos de 3 segundos entre peticiones (scripts, hojas de estilo, imágenes, etc.):

`wget {{[-pkw|--page-requisites --convert-links --wait]}} 3 {{https://example.com/some_page.html}}`

- Descarga todos los archivos listados en un directorio y sus subdirectorios (no descarga elementos embebidos):

`wget {{[-mnp|--mirror --no-parent]}} {{https://example.com/ruta/}}`

- Limita la velocidad de descarga y el número de reintentos de conexión:

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/ruta/}}`

- Descarga un archivo de un servidor HTTP usando autenticación básica (también funciona con FTP):

`wget --user {{usuario}} --password {{contraseña}} {{https://example.com}}`

- Continúa una descarga incompleta:

`wget {{[-c|--continue]}} {{https://example.com}}`

- Descarga todas las URLs almacenadas en un archivo de texto a un directorio específico:

`wget {{[-P|--directory-prefix]}} {{ruta/al/directorio}} {{[-i|--input-file]}} {{ruta/a/URLs.txt}}`
