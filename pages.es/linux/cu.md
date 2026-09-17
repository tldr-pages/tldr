# cu

> Llama a otro sistema y actúa como terminal de marcado/serie o realiza transferencias de archivos sin comprobación de errores.
> Vea también: `picocom`, `minicom`, `tio`.
> Más información: <https://manned.org/cu>.

- Abre un puerto serie determinado:

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}}`

- Abre un puerto serie determinado con una velocidad de transmisión determinada:

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{115200}}`

- Abre un puerto serie determinado con una velocidad de transmisión determinada y repite los caracteres localmente (modo semidúplex):

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{115200}} {{[-h|--halfduplex]}}`

- Abre un puerto serie determinado con una velocidad de transmisión determinada, paridad y sin control de flujo de hardware o software:

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{115200}} --parity={{even|odd|none}} {{[-f|--nortscts]}} --nostop`

- Sale de la sesión `cu` cuando está conectado:

`<Intro><~><.>`

- Muestra la ayuda:

`cu --help`
