# avrdude

> Meghajtóprogram az Atmel AVR mikrokontrollerek programozásához. További információ: <https://www.nongnu.org/avrdude/>.

- Olvassa el AVR mikrokontroller:

`avrdude -p {{AVR_device}} -c {{programmer}} -U flash:r:{{file.hex}}:i`

- AVR mikrokontroller írása:

`avrdude -p {{AVR_device}} -c {{programmer}} -U flash:w:{{file.hex}}`

- Az elérhető AVR eszközök listája:

`avrdude -p \?`

- Az elérhető AVR programozók listája:

`avrdude -c \?`
