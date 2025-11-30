# picotool

> Manage Raspberry Pi Pico boards.
> More information: <https://github.com/raspberrypi/picotool#overview>.

- Display information about the currently loaded program on a Pico:

`picotool info`

- Load a binary onto a Pico:

`picotool load {{path/to/binary}}`

- Convert an ELF or BIN file to UF2:

`picotool uf2 convert {{path/to/elf_or_bin}} {{path/to/output}}`

- Reboot a Pico:

`picotool reboot`

- List all known registers:

`picotool otp list`

- Display version:

`picotool version`

- Display help:

`picotool help`
