# picocom

> Programa minimalista para emular consolas serie.
> Más información: <https://manned.org/picocom>.

- Conecta a una consola serie con una velocidad en baudios específica:

`picocom {{/dev/ttyXYZ}} --baud {{baud_rate}}`

- Asigna caracteres especiales (por ejemplo, `LF` a `CRLF`):

`picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}}`
