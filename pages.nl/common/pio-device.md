# pio device

> Beheer en monitor PlatformIO apparaten.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/device/>.

- Toon alle beschikbare seriële poorten:

`pio device list`

- Toon alle beschikbare logische apparaten:

`pio device list --logical`

- Start een interactieve apparaat monitor:

`pio device monitor`

- Start een interactieve apparaat monitor en luister naar een specifieke poort:

`pio device monitor {{[-p|--port]}} {{/dev/ttyUSBX}}`

- Start een interactieve apparaat monitor en stel een specifieke baud in (standaard is 9600):

`pio device monitor {{[-b|--baud]}} {{57600}}`

- Start een interactieve apparaat monitor en stel een specifieke EOL karakter in (standaard is `CRLF`):

`pio device monitor --eol {{CRLF|CR|LF}}`

- Ga naar het menu van de interactieve apparaat monitor:

`<Ctrl t>`
