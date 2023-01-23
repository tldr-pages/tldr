# st-flash

> Bináris fájlok flashelése STM32 ARM Cortex mikrokontrollerekre. További információ: <https://github.com/texane/stlink>.

- Olvasson be 4096 bájtot az eszközről 0x8000000-tól kezdve:

`st-flash read {{firmware}}.bin {{0x8000000}} {{4096}}`

- Firmware írása az eszközre 0x8000000-tól kezdve:

`st-flash write {{firmware}}.bin {{0x8000000}}`

- Firmware törlése az eszközről:

`st-flash erase`
