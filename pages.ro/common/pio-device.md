# pio device

> Gestionați și monitorizați dispozitivele PlatForMio.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/device/>

- Listează toate porturile seriale disponibile:

`pio device list`

- Listează toate dispozitivele logice disponibile:

`pio device list --logical`

- Porniți un monitor de dispozitiv interactiv:

`pio device monitor`

- Porniți un monitor de dispozitiv interactiv și ascultați un anumit port:

`pio device monitor --port {{/dev/ttyUSBX}}`

- Porniți un monitor de dispozitiv interactiv și setați o rată de baud specifică (implicit la 9600):

`pio device monitor --baud {{57600}}`

- Porniți un monitor de dispozitiv interactiv și setați un anumit caracter EOL (implicit la `CRLF'):

`pio device monitor --eol {{CRLF|CR|LF}}`

- Accesați meniul monitorului dispozitivului interactiv:

`Ctrl + T`
