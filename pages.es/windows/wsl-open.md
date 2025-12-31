# wsl-open

> Abre un archivo o URL desde el Subsistema de Windows para Linux en la aplicación GUI predeterminada de Windows del usuario.
> Más información: <https://gitlab.com/4U6U57/wsl-open>.

- Abre el directorio actual en el Explorador de Windows:

`wsl-open {{.}}`

- Abre una URL en el navegador web predeterminado del usuario en Windows:

`wsl-open {{https://example.com}}`

- Abre un archivo específico en la aplicación predeterminada del usuario en Windows:

`wsl-open {{ruta\al\archivo}}`

- Establece `wsl-open` como el navegador web del shell (abre enlaces con `wsl-open`):

`wsl-open -w`

- Muestra la ayuda:

`wsl-open -h`
