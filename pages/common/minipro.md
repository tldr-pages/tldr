# minipro

> Command-line program for controlling Xgecu chip programmers (TL866A/CS, TL866II+, T48, T56).
> Supports reading, writing, and verifying various chips including AVRs, PICs, microcontrollers, and memory chips.
> More information: <https://manned.org/minipro>.

- List all supported devices:

`minipro {{[-l|--list]}}`

- Search for a specific device:

`minipro {{[-L|--search]}} {{device_name}}`

- Read chip ID:

`minipro {{[-p|--device]}} {{chip_name}} {{[-D|--read_id]}}`

- Read chip contents to a file:

`minipro --device {{chip_name}} --read {{path/to/output_file.bin}}`

- Write a file to chip:

`minipro --device {{chip_name}} --write {{path/to/input_file.bin}}`

- Verify chip contents against a file:

`minipro --device {{chip_name}} --verify {{path/to/file.bin}}`

- Erase a chip:

`minipro --device {{chip_name}} --erase`

- Display help:

`minipro --help`
