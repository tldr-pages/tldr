# tasklist

> A helyi vagy távoli gépen jelenleg futó folyamatok listájának megjelenítése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- Jelenleg futó folyamatok megjelenítése:

`tasklist`

- A futó folyamatok megjelenítése egy megadott kimeneti formátumban:

`tasklist /fo {{table|list|csv}}`

- A futó folyamatok megjelenítése a megadott `.exe` vagy `.dll` fájlnév használatával:

`tasklist /m {{module_pattern}}`

- Távoli gépen futó folyamatok megjelenítése:

`tasklist /s {{remote_name}} /u {{username}} /p {{password}}`

- Az egyes folyamatokat használó szolgáltatások megjelenítése:

`tasklist /svc`
