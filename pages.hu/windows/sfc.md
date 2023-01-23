# sfc

> Ellenőrzi a Windows rendszerfájlok integritását. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>.

- A parancs használatára vonatkozó információk megjelenítése:

`sfc`

- Az összes rendszerfájl átvizsgálása és lehetőség szerint a problémák javítása:

`sfc /scannow`

- Az összes rendszerfájl beolvasása anélkül, hogy megpróbálná javítani valamelyiket:

`sfc /verifyonly`

- Egy adott fájl átvizsgálása és, ha lehetséges, a problémák javítása:

`sfc /scanfile={{path/to/file}}`

- Egy adott fájl beolvasása anélkül, hogy megpróbálná javítani:

`sfc /verifyfile={{path/to/file}}`

- Offline javítás esetén adja meg a rendszerindító könyvtárat:

`sfc /offbootdir={{path/to/directory}}`

- Offline javításkor adja meg a Windows könyvtárat:

`sfc /offwindir={{path/to/directory}}`
