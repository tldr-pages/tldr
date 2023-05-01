# avrdude

> Programa controlador para la programación de microcontroladores Atmel AVR.
> Más información: <https://www.nongnu.org/avrdude/>.

- Lee el microcontrolador AVR:

`avrdude -p {{AVR_dispositivo}} -c {{programador}} -U flash:r:{{file.hex}}:i`

- Escribe el microcontrolador AVR:

`avrdude -p {{AVR_dispositivo}} -c {{programador}} -U flash:w:{{file.hex}}`

- Lista de dispositivos AVR disponibles:

`avrdude -p \?`

- Lista de programadores AVR disponibles:

`avrdude -c \?`
