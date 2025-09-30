# fatrace

> Informa de eventos de acceso a archivos.
> Más información: <https://manned.org/fatrace>.

- Imprime en `stdout` los eventos de acceso a archivos en todos los sistemas de archivos montados:

`sudo fatrace`

- Imprime en `stdout` eventos de acceso a archivos en el montaje del directorio actual, con marcas de tiempo:

`sudo fatrace {{[-c|--current-mount]}} {{[-t|--timestamp]}}`
