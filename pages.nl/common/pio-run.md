# pio run

> Voer PlatformIO project doelen uit.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>.

- Toon alle beschikbare project doelen:

`pio run --list-targets`

- Toon alle beschikbare project doelen voor een specifieke omgeving:

`pio run --list-targets --environment {{omgeving}}`

- Voer alle doelen uit:

`pio run`

- Voer alle doelen uit voor de gespecificeerde omgevingen:

`pio run --environment {{omgeving1}} --environment {{omgeving2}}`

- Voer gespecificeerde doelen uit:

`pio run --target {{doel1}} --target {{doel2}}`

- Voer de doelen uit van een specifiek configuratiebestand:

`pio run --project-conf {{pad/naar/platformio.ini}}`
