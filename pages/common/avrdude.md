# avrdude

> Driver program for Atmel AVR microcontrollers programming.
> More information: <https://www.nongnu.org/avrdude/>.

- Read AVR microcontroller:

`avrdude -p {{AVR_device}} -c {{programmer}} -U flash:r:{{file.hex}}:i`

- Write AVR microcontroller:

`avrdude -p {{AVR_device}} -c {{programmer}} -U flash:w:{{file.hex}}`

- List available AVR devices:

`avrdude -p \?`

- List available AVR programmers:

`avrdude -c \?`
