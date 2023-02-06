# Get-FileHash

> Hash kiszámítása egy fájlhoz. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- SHA256 algoritmus segítségével kiszámítja egy megadott fájl kivonatát:

`Get-FileHash {{path/to/file}}`

- Megadott fájl hash-értékének kiszámítása egy megadott algoritmus segítségével:

`Get-FileHash {{path/to/file}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`
