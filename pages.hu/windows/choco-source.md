# choco source

> Csomagok forrásainak kezelése a Chocolatey segítségével. További információ: <https://chocolatey.org/docs/commands-source>.

- A jelenleg elérhető források listája:

`choco source list`

- Új csomagforrás hozzáadása:

`choco source add --name {{name}} --source {{url}}`

- Új csomagforrás hozzáadása hitelesítő adatokkal:

`choco source add --name {{name}} --source {{url}} --user {{username}} --password {{password}}`

- Új csomagforrás hozzáadása ügyféltanúsítvánnyal:

`choco source add --name {{name}} --source {{url}} --cert {{path/to/certificate}}`

- Csomagforrás engedélyezése:

`choco source enable --name {{name}}`

- Csomagforrás letiltása:

`choco source disable --name {{name}}`

- Csomagforrás eltávolítása:

`choco source remove --name {{name}}`
