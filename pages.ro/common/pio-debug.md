# pio debug

> Proiecte de depanare PlatForMio.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>

- Depanați proiectul PlatForMio în directorul curent:

`pio debug`

- Depanați un anumit proiect PlatForMio:

`pio debug --project-dir {{path/to/platformio_project}}`

- Depanarea unui mediu specific:

`pio debug --environment {{environment}}`

- Depanați un proiect PlatForMio folosind un fișier de configurare specific:

`pio debug --project-conf {{path/to/platformio.ini}}`

- Depanarea unui proiect PlatForMio folosind depanatorul `gdb`:

`pio debug --interface={{gdb}} {{gdb_options}}`
