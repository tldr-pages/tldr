# pio debug

> Debug PlatformIO projecten.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

- Debug het PlatformIO project in de huidige map:

`pio debug`

- Debug een specifiek PlatformIO project:

`pio debug --project-dir {{pad/naar/platformio_project}}`

- Debug een specifieke omgeving:

`pio debug --environment {{omgeving}}`

- Debug een PlatformIO project met een specifiek configuratiebestand:

`pio debug --project-conf {{pad/naar/platformio.ini}}`

- Debug een PlatformIO project door gebruik te maken van de `gdb` debugger:

`pio debug --interface={{gdb}} {{gdb_opties}}`
