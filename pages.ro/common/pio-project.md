# pio project

> Instrument pentru gestionarea proiectelor PlatForMio.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/project/>

- Inițializarea unui nou proiect PlatForMio:

`pio project init`

- Inițializarea unui nou proiect PlatForMio într-un anumit director:

`pio project init --project-dir {{path/to/project_directory}}`

- Inițializarea unui nou proiect PlatForMio, specificând un ID de bord:

`pio project init --board {{ATmega328P|uno|...}}`

- Inițializarea unui nou proiect bazat pe PlatForMio, specificând una sau mai multe opțiuni de proiect:

`pio project init --project-option="{{option}}={{value}}" --project-option="{{option}}={{value}}"`

- Imprimați configurația unui proiect:

`pio project config`
