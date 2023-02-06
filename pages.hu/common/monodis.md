# monodis

> A Mono Common Intermediate Language (CIL) disassembler. További információ: <https://www.mono-project.com/docs/tools+libraries/tools/monodis/>.

- Egy assembly szétszerelése szöveges CIL-é:

`monodis {{path/to/assembly.exe}}`

- A kimenet mentése egy fájlba:

`monodis --output={{path/to/output.il}} {{path/to/assembly.exe}}`

- Információk megjelenítése egy assemblyről:

`monodis --assembly {{path/to/assembly.dll}}`

- Egy összeállítás hivatkozásainak listázása:

`monodis --assemblyref {{path/to/assembly.exe}}`

- Egy assembly összes metódusának listázása:

`monodis --method {{path/to/assembly.exe}}`

- A szerelvénybe ágyazott erőforrások listájának megjelenítése:

`monodis --manifest {{path/to/assembly.dll}}`

- Az összes beágyazott erőforrás kivonása az aktuális könyvtárba:

`monodis --mresources {{path/to/assembly.dll}}`
