# ddcutil

> A csatlakoztatott kijelzők beállításainak vezérlése DDC/CI-n keresztül. Ehhez a parancshoz a `i2c-dev` kernelmodul betöltése szükséges. Lásd még: `modprobe`. További információ: <https://www.ddcutil.com>.

- Az összes kompatibilis kijelző listázása:

`ddcutil detect`

- Az 1. kijelző fényerejének (0x10 opció) 50%-ra történő módosítása:

`ddcutil --display {{1}} setvcp {{10}} {{50}}`

- Növelje az 1. kijelző kontrasztját (0x12 opció) 5%-kal:

`ddcutil -d {{1}} setvcp {{12}} {{+}} {{5}}`

- Olvassa be az 1. kijelző beállításait:

`ddcutil -d {{1}} getvcp {{ALL}}`
