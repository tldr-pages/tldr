# pio վրիպազերծում

> Վրիպազերծել PlatformIO նախագծերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>:.

- Վրիպազերծել PlatformIO նախագիծը ընթացիկ գրացուցակում.:

`pio debug`

- Վրիպազերծել կոնկրետ PlatformIO նախագիծ.:

`pio debug {{[-d|--project-dir]}} {{path/to/platformio_project}}`

- Որոշակի միջավայրի վրիպազերծում.:

`pio debug {{[-e|--environment]}} {{environment}}`

- Վրիպազերծել PlatformIO նախագիծը՝ օգտագործելով հատուկ կազմաձևման ֆայլ.:

`pio debug {{[-c|--project-conf]}} {{path/to/platformio.ini}}`

- Վրիպազերծել PlatformIO նախագիծը՝ օգտագործելով `gdb` վրիպազերծիչը.:

`pio debug --interface {{gdb}} {{gdb_options}}`
