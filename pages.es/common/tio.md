# tio

> Supervisa e interactúa con puertos serie.
> Vea también: `picocom`, `cu`, `minicom`.
> Más información: <https://github.com/tio/tio#3-usage>.

- Abre un puerto serie con la configuración predeterminada:

`tio {{/dev/ttyUSB0}}`

- Abre un puerto serie con una velocidad de transmisión específica:

`tio {{[-b|--baudrate]}} {{9600}} {{/dev/ttyUSB0}}`

- Abre un puerto serie y registra la salida en un archivo:

`tio {{[-L|--log]}} --log-file {{archivo_de_registro}} {{/dev/ttyUSB0}}`

- Abre un puerto serie y habilita la salida hexadecimal:

`tio --output-mode hex {{/dev/ttyUSB0}}`

- Muestra los puertos serie disponibles:

`tio {{[-l|--list]}}`

- Sale de la sesión `tio`:

`<Ctrl t><q>`
