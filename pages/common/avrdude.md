# avrdude

> Driver program for Atmel AVR microcontrollers programming.
> More information: <https://www.nongnu.org/avrdude/>.

- [r]ead the flash ROM of a AVR microcontroller with a specific [p]art ID:

`avrdude -p {{part_no}} -c {{programmer_id}} -U flash:r:{{file.hex}}:i`

- [w]rite to the flash ROM AVR microcontroller:

`avrdude -p {{part_no}} -c {{programmer}} -U flash:w:{{file.hex}}`

- List available AVR devices:

`avrdude -p \?`

- List available AVR programmers:

`avrdude -c \?`
