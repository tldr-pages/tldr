# pio debug

> PlatformIO projektek hibakeresése. További információ: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

- A PlatformIO projekt hibakeresése az aktuális könyvtárban:

`pio debug`

- Egy adott PlatformIO projekt hibakeresése:

`pio debug --project-dir {{path/to/platformio_project}}`

- Egy adott környezet hibakeresése:

`pio debug --environment {{environment}}`

- PlatformIO projekt hibakeresése egy adott konfigurációs fájl használatával:

`pio debug --project-conf {{path/to/platformio.ini}}`

- PlatformIO projekt hibakeresése a `gdb` debugger használatával:

`pio debug --interface={{gdb}} {{gdb_options}}`
