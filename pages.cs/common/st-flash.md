# st-flash

> Nahrává binární soubory do STM32 ARM Cortex mikrořadičů.
> Více informací: <https://manned.org/st-flash>.

- Přečíst 4096 bajtů ze zařízení začínající od 0x8000000:

`st-flash read {{firmware}}.bin 0x8000000 4096`

- Zapsat firmware do zařízení začínající od 0x8000000:

`st-flash write {{firmware}}.bin 0x8000000`

- Vymazat firmware ze zařízení:

`st-flash erase`
