# avrdude

> Program ovladače pro programování Atmel AVR mikrořadičů.
> Více informací: <https://www.nongnu.org/avrdude/user-manual/avrdude_3.html#Option-Descriptions>.

- P[r]ečíst flash ROM AVR mikrořadiče s konkrétním ID součástky:

`avrdude -p {{cislo_soucastky}} -c {{id_programatora}} -U flash:r:{{soubor.hex}}:i`

- Zapsat do flash ROM AVR mikrořadiče:

`avrdude -p {{cislo_soucastky}} -c {{programator}} -U flash:w:{{file.hex}}`

- Vypsat dostupné AVR zařízení:

`avrdude -p \?`

- Vypsat dostupné AVR programátory:

`avrdude -c \?`
