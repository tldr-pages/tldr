# minicom

> Se comunica con la interfaz serie de un dispositivo.
> Vea también: `picocom`, `cu`, `tio`.
> Más información: <https://manned.org/minicom>.

- Abre un puerto serie determinado:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}}`

- Abre un puerto serie determinado con una velocidad de transmisión determinada:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}} {{[-b|--baudrate]}} {{115200}}`

- Accede al menú de configuración antes de comunicarse con un puerto serie determinado:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}} {{[-s|--setup]}}`

- Captura la salida de un puerto serie en un archivo:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}} {{[-C|--capturefile]}} {{ruta/a/archivo}}`

- Sale de minicom:

`<Ctrl a><x><Enter>`

- Muestra la ayuda:

`minicom {{[-h|--help]}}`
