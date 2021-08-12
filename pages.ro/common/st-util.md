# st-util

> Executați GDB (GNU Debugger) server pentru a interacționa cu STM32 ARM Cortex microcontoller.
> Mai multe informaţii: <https://github.com/texane/stlink>

- Run server GDB pe portul 4500:

`st-util -p {{4500}}`

- Conectează-te la serverul GDB:

`(gdb) target extended-remote {{localhost}}:{{4500}}`

- Scrie firmware-ul pe dispozitiv:

`(gdb) load {{firmware.elf}}`
