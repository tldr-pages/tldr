# pio run

> Rulați obiectivele proiectului PlatForMio.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>

- Listează toate obiectivele disponibile ale proiectului:

`pio run --list-targets`

- Listează toate obiectivele de proiect disponibile pentru un anumit mediu:

`pio run --list-targets --environment {{environment}}`

- Rulaţi toate ţintele:

`pio run`

- Rulați toate țintele mediilor specificate:

`pio run --environment {{environment1}} --environment {{environment2}}`

- Rulați țintele specificate:

`pio run --target {{target1}} --target {{target2}}`

- Rulați obiectivele unui fișier de configurare specificat:

`pio run --project-conf {{path/to/platformio.ini}}`
