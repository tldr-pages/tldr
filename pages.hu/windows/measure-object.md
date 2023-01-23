# Measure-Object

> Kiszámítja az objektumok numerikus tulajdonságait, valamint a karaktereket, szavakat és sorokat a karakterlánc-objektumokban, például szövegfájlokban. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/measure-object>.

- Megszámolja a fájlokat és mappákat egy könyvtárban:

`Get-ChildItem | Measure-Object`

- Pipe input a Measure-Command parancsba (a `Measure-Command` címre pipázott objektumok a Expression paraméterhez átadott szkriptblokk számára elérhetőek):

`"One", "Two", "Three", "Four" | Set-Content -Path "{{path/to/file}}"; Get-Content "{{path/to/file}}"; | Measure-Object -Character -Line -Word`
