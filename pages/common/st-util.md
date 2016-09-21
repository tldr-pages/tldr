# st-util

> Run GDB (GNU Debugger) server to interact with STM32 ARM Cortex microcontoller.

- Run GDB server on port 4500:

`st-util -p {{4500}}`

- Connect to GDB server:

`(gdb) target extended-remote {{localhost}}:{{4500}}`

- Write firmware to device:

`(gdb) load {{firmware.elf}}`
