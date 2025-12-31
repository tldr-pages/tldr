# picocom

> Programa minimalista para emular consolas serie.
> Más información: <https://manned.org/picocom>.

- Conecta a una consola serie con una velocidad en baudios específica:

`picocom {{/dev/ttyXYZ}} {{[-b|--baud]}} {{tasa_de_baudios}}`

- Asigna caracteres especiales (p. ej. `LF` a `CRLF`):

`picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`
