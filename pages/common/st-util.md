# st-util

> Run GDB (GNU Debugger) server to interact with STM32 ARM Cortex microcontoller.
> More information: <https://github.com/stlink-org/stlink/blob/testing/doc/man/st-util.md>.

- Run GDB server on port 4500:

`st-util {{[-p|--listen_port]}} {{4500}}`

- Connect to GDB server within `gdb`:

`target extended-remote {{localhost}}:{{4500}}`

- Write firmware to device:

`load {{firmware.elf}}`
