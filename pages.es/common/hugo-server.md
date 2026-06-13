# hugo server

> Construye y publica un sitio con el servidor web integrado de Hugo.
> Más información: <https://gohugo.io/commands/hugo_server/>.

- Construye y publica un sitio:

`hugo server`

- Construye y publica un sitio en un número de puerto especificado:

`hugo server {{[-p|--port]}} {{número_de_puerto}}`

- Construye y publica un sitio mientras se minimizan los formatos de salida soportados (HTML, XML, etc.):

`hugo server --minify`

- Construye y sirve un sitio en el entorno de producción con reconstrucción completa (re-render) disminuyendo el tamaño (minify) en los formatos soportados:

`hugo server {{[-e|--environment]}} {{producción}} --disableFastRender --minify`

- Muestra la ayuda:

`hugo server {{[-h|--help]}}`
