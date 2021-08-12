# pio test

> Rulați teste locale pe un proiect PlatForMio.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>

- Rulați toate testele în toate mediile proiectului PlatForMio curent:

`pio test`

- Testați numai medii specifice:

`pio test --environment {{environment1}} --environment {{environment2}}`

- Rulați numai teste al căror nume se potrivește cu un anumit model glob:

`pio test --filter "{{pattern}}"`

- Ignorați testele al căror nume se potrivește cu un anumit model glob:

`pio test --ignore "{{pattern}}"`

- Specificați un port pentru încărcarea firmware-ului:

`pio test --upload-port {{upload_port}}`

- Specificați un fișier de configurare personalizat pentru rularea testelor:

`pio test --project-conf {{path/to/platformio.ini}}`
