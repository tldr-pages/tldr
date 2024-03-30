# pio check

> Voer een statische analyse check uit op een PlatformIO project.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>.

- Voer een basis analyse check uit op het huidige project:

`pio check`

- Voer een basis analyse check uit op een specifiek project:

`pio check --project-dir {{project_map}}`

- Voer een analyse check uit voor een specifieke omgeving:

`pio check --environment {{omgeving}}`

- Voer een analyse check uit en rapporteer alleen een specifiek niveau:

`pio check --severity {{low|medium|high}}`

- Voer een analyse check uit en toon gedetailleerde informatie bij het verwerken van omgevingen:

`pio check --verbose`
