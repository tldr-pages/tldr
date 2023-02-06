# pio system

> Különféle rendszerparancsok a PlatformIO számára. További információ: <https://docs.platformio.org/en/latest/core/userguide/system/>.

- Shell-kiegészítő telepítése az aktuális shellhez (támogatja a Bash, Fish, Zsh és PowerShell parancsokat):

`pio system completion install`

- A shell-kiegészítés eltávolítása az aktuális shellhez:

`pio system completion uninstall`

- A PlatformIO egész rendszerre kiterjedő információinak megjelenítése:

`pio system info`

- A nem használt PlatformIO adatok eltávolítása:

`pio system prune`

- Csak a gyorsítótárban tárolt adatok eltávolítása:

`pio system prune --cache`

- A nem használt PlatformIO-adatok listázása, amelyek eltávolításra kerülnének, de valójában nem távolítja el őket:

`pio system prune --dry-run`
