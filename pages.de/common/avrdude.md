# avrdude

> Treiberprogramm für Atmel AVR Mikrocontroller-Programmierung.
> Weitere Information: <https://www.nongnu.org/avrdude/>.

- Schreibt Speicherinhalt des AVR Mikrocontrollers in datei.hex:

`avrdude -p {{AVR_gerät}} -c {{programmer}} -U flash:r:{{datei.hex}}:i`

- Schreibt den Inhalt von datei.hex in den AVR Mikrocontroller:

`avrdude -p {{AVR_gerät}} -c {{programmer}} -U flash:w:{{datei.hex}}`

- Liste alle verfügbaren AVR Geräte auf:

`avrdude -p \?`

- Liste alle verfügbaren AVR Programmer auf:

`avrdude -c \?`
