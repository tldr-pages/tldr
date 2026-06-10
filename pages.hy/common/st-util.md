# st-util

> Գործարկեք GDB (GNU Debugger) սերվերը՝ STM32 ARM Cortex միկրոկոնտոլերի հետ փոխազդելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/stlink-org/stlink/blob/testing/doc/man/st-util.md>:.

- Գործարկեք GDB սերվերը 4500 նավահանգստում.:

`st-util {{[-p|--listen_port]}} {{4500}}`

- [Ինտերակտիվ] Միացեք GDB սերվերին `gdb`-ի սահմաններում.:

`target extended-remote {{localhost}}:{{4500}}`

- [Ինտերակտիվ] Գրեք որոնվածը սարքին.:

`load {{firmware.elf}}`
