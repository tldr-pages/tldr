# picotool

> Կառավարեք Raspberry Pi Pico-ի տախտակները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/raspberrypi/picotool#overview>:.

- Ցուցադրել տեղեկատվություն ներկայումս բեռնված ծրագրի մասին Pico-ում.:

`picotool info`

- Բեռնել երկուականը Pico-ի վրա.:

`picotool load {{path/to/binary}}`

- Վերափոխեք ELF կամ BIN ֆայլը UF2:

`picotool uf2 convert {{path/to/elf_or_bin}} {{path/to/output}}`

- Վերագործարկեք Pico:

`picotool reboot`

- Թվարկեք բոլոր հայտնի գրանցամատյանները.:

`picotool otp list`

- Ցուցադրել օգնությունը.:

`picotool help`

- Ցուցադրման տարբերակը:

`picotool version`
