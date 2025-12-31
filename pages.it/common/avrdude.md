# avrdude

> Driver per il programmatore di microcontrollori Atmel AVR.
> Maggiori informazioni: <https://www.nongnu.org/avrdude/user-manual/avrdude_3.html#Option-Descriptions>.

- Leggi dal microcontrollore AVR:

`avrdude -p {{dispositivo_AVR}} -c {{id_programmatore}} -U flash:r:{{file.hex}}:i`

- Scrivi sul microcontrollore AVR:

`avrdude -p {{dispositivo_AVR}} -c {{id_programmatore}} -U flash:w:{{file.hex}}`

- Elenca dispositivi AVR disponibili:

`avrdude -p \?`

- Elenca programmatori AVR disponibili:

`avrdude -c \?`
