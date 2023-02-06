# pio device

> PlatformIO eszközök kezelése és felügyelete. További információ: <https://docs.platformio.org/en/latest/core/userguide/device/>.

- Az összes rendelkezésre álló soros port listázása:

`pio device list`

- Az összes rendelkezésre álló logikai eszköz listázása:

`pio device list --logical`

- Interaktív eszközmonitor indítása:

`pio device monitor`

- Interaktív eszközmonitor indítása és egy adott port meghallgatása:

`pio device monitor --port {{/dev/ttyUSBX}}`

- Interaktív eszközmonitor indítása és egy adott baud-ráta beállítása (alapértelmezett 9600):

`pio device monitor --baud {{57600}}`

- Interaktív eszközmonitor indítása és egy adott EOL karakter beállítása (alapértelmezett: `CRLF`):

`pio device monitor --eol {{CRLF|CR|LF}}`

- Az interaktív eszközmonitor menüjének megnyitása:

`Ctrl + T`
