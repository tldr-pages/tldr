# avrdude

> Program de driver pentru programarea microcontrolere Atmel AVR.
> Mai multe informaţii: <https://www.nongnu.org/avrdude/>

- Citește microcontroler AVR:

`avrdude -p {{AVR_device}} -c {{programmer}} -U flash:r:{{file.hex}}:i`

- Scrie microcontroler AVR:

`avrdude -p {{AVR_device}} -c {{programmer}} -U flash:w:{{file.hex}}`

- Lista dispozitivelor AVR disponibile:

`avrdude -p \?`

- Lista programatorilor AVR disponibile:

`avrdude -c \?`
