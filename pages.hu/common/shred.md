# shred

> Fájlok felülírása az adatok biztonságos törléséhez. További információ: <https://www.gnu.org/software/coreutils/shred>.

- Fájlok felülírása:

`shred {{path/to/file}}`

- Fájl felülírása, véletlenszerű adatok helyett nullákat hagyva:

`shred --zero {{path/to/file}}`

- Egy fájl 25-szörös felülírása:

`shred -n25 {{path/to/file}}`

- Fájl felülírása és eltávolítása:

`shred --remove {{path/to/file}}`
