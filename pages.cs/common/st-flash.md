# st-flash

> Nahrává binární soubory do STM32 ARM Cortex mikrořadičů.
> Více informací: <https://github.com/stlink-org/stlink/blob/testing/doc/man/st-flash.md>.

- Přečíst 4096 bajtů ze zařízení začínající od 0x8000000:

`st-flash read {{firmware}}.bin 0x8000000 4096`

- Zapsat firmware do zařízení začínající od 0x8000000:

`st-flash write {{firmware}}.bin 0x8000000`

- Vymazat firmware ze zařízení:

`st-flash erase`
