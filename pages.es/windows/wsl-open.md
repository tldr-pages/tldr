# wsl-open

> Abre un archivo o URL desde el Subsistema de Windows para Linux en la aplicación GUI predeterminada de Windows del usuario.
> Más información: <https://gitlab.com/4U6U57/wsl-open>.

- Abrir el directorio actual en el Explorador de Windows:

`wsl-open {{.}}`

- Abrir una URL en el navegador web predeterminado del usuario en Windows:

`wsl-open {{https://ejemplo.com}}`

- Abrir un archivo específico en la aplicación predeterminada del usuario en Windows:

`wsl-open {{ruta\al\archivo}}`

- Establecer `wsl-open` como el navegador web del shell (abre enlaces con `wsl-open`):

`wsl-open -w`

- Mostrar ayuda:

`wsl-open -h`
