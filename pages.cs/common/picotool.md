# picotool

> Spravuje desky Raspberry Pi Pico.
> Více informací: <https://github.com/raspberrypi/picotool>.

- Zobrazit informace o aktuálně načteném programu na Picu:

`picotool info`

- Načíst binárku do Pica:

`picotool load {{cesta/k/binarce}}`

- Převést soubor ELF nebo BIN na UF2:

`picotool uf2 convert {{cesta/k/elf_nebo_bin}} {{cesta/k/vystupu}}`

- Restartovat Pico:

`picotool reboot`

- Vypsat všechny známe registry:

`picotool otp list`

- Zobrazit verzi:

`picotool version`

- Zobrazit nápovědu:

`picotool help`
