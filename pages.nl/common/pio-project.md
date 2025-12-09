# pio project

> Beheer PlatformIO projecten.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/project/>.

- Initialiseer een nieuw PlatformIO project:

`pio project init`

- Initialiseer een nieuw PlatformIO project in een specifieke map:

`pio project init {{[-d|--project-dir]}} {{pad/naar/project_map}}`

- Initialiseer een nieuw PlatformIO project, met een gespecificeerd board ID:

`pio project init {{[-b|--board]}} {{ATmega328P|uno|...}}`

- Initialiseer een nieuw PlatformIO gebaseerd project, met een of meerdere gespecificeerde project opties:

`pio project init {{[-O|--project-option]}} "{{optie}}={{waarde}}" {{[-O|--project-option]}} "{{optie}}={{waarde}}"`

- Toon de configuratie van een project:

`pio project config`
