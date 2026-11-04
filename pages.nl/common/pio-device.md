# pio device

> Beheer en monitor PlatformIO apparaten.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/device/>.

- Toon alle beschikbare seriële poorten:

`pio device list`

- Toon alle beschikbare logische apparaten:

`pio device list --logical`

- Start een interactieve apparaatmonitor:

`pio device monitor`

- Start een interactieve apparaatmonitor en luister naar een specifieke poort:

`pio device monitor {{[-p|--port]}} {{/dev/ttyUSBX}}`

- Start een interactieve apparaatmonitor en stel een specifieke baud in (standaard is 9600):

`pio device monitor {{[-b|--baud]}} {{57600}}`

- Start een interactieve apparaatmonitor en stel een specifiek EOL-karakter in (standaard is `CRLF`):

`pio device monitor --eol {{CRLF|CR|LF}}`

- Ga naar het menu van de interactieve apparaatmonitor:

`<Ctrl t>`
