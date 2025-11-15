# cu

> Llama a otro sistema y actúa como terminal de marcado/serie o realiza transferencias de archivos sin comprobación de errores.
> Más información: <https://manned.org/cu>.

- Abre un puerto serie determinado:

`sudo cu {{[-l|--line]}} {{/dev/ttyUSB0}}`

- Abre un puerto serie determinado con una velocidad en baudios determinada:

`sudo cu {{[-l|--line]}} {{/dev/ttyUSB0}} {{[-s|--speed]}} {{115200}}`

- Abre un puerto serie determinado con una velocidad en baudios determinada y emite un eco de caracteres localmente (modo semidúplex):

`sudo cu {{[-l|--line]}} {{/dev/ttyUSB0}} {{[-s|--speed]}} {{115200}} {{[-h|--halfduplex]}}`

- Abre un puerto serie determinado con una velocidad en baudios, paridad y sin control de flujo por hardware o software:

`sudo cu {{[-l|--line]}} {{/dev/ttyUSB0}} {{[-s|--speed]}} {{115200}} --parity={{par|odd|none}} {{[-f|--nortscts]}} --nostop`

- Sale de la sesión `cu` cuando está conectado:

`<Enter><~><.>`
