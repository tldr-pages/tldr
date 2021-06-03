# avrdude

> Treiberprogramm für Atmel AVR Mikrocontroller-Programmierung.
> Weitere Informationen: <https://www.nongnu.org/avrdude/>.

- Schreibt den Speicherinhalt eines AVR-Mikrocontrollers in eine Datei:

`avrdude -p {{avr_gerät}} -c {{programmer}} -U flash:r:{{pfad/zu/datei.hex}}:i`

- Schreibt den Inhalt einer Datei in einen AVR-Mikrocontroller:

`avrdude -p {{avr_gerät}} -c {{programmer}} -U flash:w:{{pfad/zu/datei.hex}}`

- Liste alle verfügbaren AVR-Geräte auf:

`avrdude -p \?`

- Liste alle verfügbaren AVR-Programmer auf:

`avrdude -c \?`
