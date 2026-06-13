# pio debug

> Debug PlatformIO projects.
> More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

- Debug the PlatformIO project in the current directory:

`pio debug`

- Debug a specific PlatformIO project:

`pio debug {{[-d|--project-dir]}} {{path/to/platformio_project}}`

- Debug a specific environment:

`pio debug {{[-e|--environment]}} {{environment}}`

- Debug a PlatformIO project using a specific configuration file:

`pio debug {{[-c|--project-conf]}} {{path/to/platformio.ini}}`

- Debug a PlatformIO project using the `gdb` debugger:

`pio debug --interface {{gdb}} {{gdb_options}}`
