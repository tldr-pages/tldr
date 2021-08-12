# pio ci

> Construiți proiecte PlatForMio cu o structură de cod sursă arbitrară.
> Acest lucru va crea un nou proiect temporar în care codul sursă va fi copiat.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>

- Construiți un proiect PlatForMio în directorul temporar implicit al sistemului și ștergeți-l după aceea:

`pio ci {{path/to/project}}`

- Construiți un proiect PlatForMio și specificați biblioteci specifice:

`pio ci --lib {{path/to/library_directory}} {{path/to/project}}`

- Construiți un proiect PlatForMio și specificați un panou specific (`pio boards` listează toate acestea):

`pio ci --board {{board}} {{path/to/project}}`

- Construiți un proiect PlatForMio într-un anumit director:

`pio ci --build-dir {{path/to/build_directory}} {{path/to/project}}`

- Construiți un proiect PlatForMio și nu ștergeți directorul de compilare:

`pio ci --keep-build-dir {{path/to/project}}`

- Construiți un proiect PlatForMio folosind un fișier de configurare specific:

`pio ci --project-conf {{path/to/platformio.ini}}`
