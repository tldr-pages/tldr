# pio debug

> Depura proyectos PlatformIO.
> Más información: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

- Depura el proyecto PlatformIO del directorio actual:

`pio debug`

- Depura un proyecto PlatformIO específico:

`pio debug --project-dir {{ruta/al/proyecto_platformio}}`

- Depura un ambiente específico:

`pio debug --environment {{ambiente}}`

- Depura un proyecto PlatformIO utilizando un archivo de configuración específico:

`pio debug --project-conf {{ruta/a/platformio.ini}}`

- Depura un proyecto PlatformIO usando el depurador `gdb`:

`pio debug --interface={{gdb}} {{opciones_de_gdb}}`
