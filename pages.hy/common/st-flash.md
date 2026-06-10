#st-flash

> Ֆլեշ երկուական ֆայլերը STM32 ARM Cortex միկրոկառավարիչներում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/stlink-org/stlink/blob/testing/doc/man/st-flash.md>:.

- Կարդացեք 4096 բայթ սարքից սկսած 0x8000000-ից.:

`st-flash read {{firmware}}.bin 0x8000000 4096`

- Գրեք որոնվածը սարքում՝ սկսած 0x8000000-ից.:

`st-flash write {{firmware}}.bin 0x8000000`

- Ջնջել որոնվածը սարքից.:

`st-flash erase`
