# minipro

> Controll Xgecu chip programmers (TL866A/CS, TL866II+, T48, T56).
> Supports various chips including AVRs, PICs, microcontrollers, and memory chips.
> More information: <https://manned.org/minipro>.

- List all supported devices:

`minipro {{[-l|--list]}}`

- Search for a specific device:

`minipro {{[-L|--search]}} {{device_name}}`

- Read chip ID:

`minipro {{[-p|--device]}} {{chip_name}} {{[-D|--read_id]}}`

- Read chip contents to a file:

`minipro {{[-p|--device]}} {{chip_name}} {{[-r|--read]}} {{path/to/output_file.bin}}`

- Write a file to chip:

`minipro {{[-p|--device]}} {{chip_name}} {{[-w|--write]}} {{path/to/input_file.bin}}`

- Verify chip contents against a file:

`minipro {{[-p|--device]}} {{chip_name}} {{[-m|--verify]}} {{path/to/file.bin}}`

- Erase a chip:

`minipro {{[-p|--device]}} {{chip_name}} {{[-E|--erase]}}`

- Display help:

`minipro {{[-h|--help]}}`
