# picotool

> Manage raspberry pi picos'.
> More information: <https://github.com/raspberrypi/picotool>.

- Display info about the currently loaded program on a pico:

`picotool info`

- Load a binary onto a pico:

`picotool load {{path/to/binary}}`

- Convert an ELF or BIN file to UF2:

`picotool uf2 convert {{path/to/elf_or_bin}} {{path/to/output}}`

- Reboot the pico:

`picotool reboot`

- List all known registers:

`picotool otp list`

- Display version:

`picotool version`

- Display help:

`picotool help`
