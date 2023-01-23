# st-util

> A GDB (GNU Debugger) szerver futtatása az STM32 ARM Cortex mikrokontrollerrel való interakcióhoz. További információ: <https://github.com/texane/stlink>.

- Futtassa a GDB szervert a 4500-as porton:

`st-util -p {{4500}}`

- Csatlakozás a GDB szerverhez:

`(gdb) target extended-remote {{localhost}}:{{4500}}`

- Firmware írása az eszközre:

`(gdb) load {{firmware.elf}}`
