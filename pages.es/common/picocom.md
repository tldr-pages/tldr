# picocom

> Programa mínimo para emular consolas serie.
> Vea también: `minicom`, `cu`, `tio`.
> Más información: <https://manned.org/picocom>.

- Se conecta a una consola serie con una velocidad de transmisión predeterminada de 9600:

`sudo picocom {{/dev/ttyXYZ}}`

- Se conecta a una consola serie con una velocidad de transmisión especificada:

`sudo picocom {{/dev/ttyXYZ}} {{[-b|--baud]}} {{tasa_de_baudios}}`

- Asigna caracteres especiales (por ejemplo, `LF` a `CRLF`):

`sudo picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`

- Sale de picocom:

`<Ctrl a><Ctrl x>`

- Muestra la ayuda:

`picocom {{[-h|--help]}}`
