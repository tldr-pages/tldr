# Resolve-Path

> Feloldja az elérési útvonalban lévő helyettesítő karaktereket, és megjeleníti az elérési útvonal tartalmát. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>.

- Feloldja a kezdőmappa elérési útvonalát:

`Resolve-Path {{~}}`

- UNC-útvonal feloldása:

`Resolve-Path -Path "\\{{hostname}}\{{path/to/file}}"`

- Relatív elérési utak lekérdezése:

`Resolve-Path -Path {{path/to/file_or_directory}} -Relative`
