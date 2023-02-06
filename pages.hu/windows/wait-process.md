# Wait-Process

> Megvárja a folyamatok leállítását, mielőtt további bemenetet fogadna. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/wait-process>.

- Egy folyamat leállítása és várakozás:

`Stop-Process -Id {{process_id}}; Wait-Process -Id {{process_id}}`

- Várakozás a folyamatokra egy megadott ideig:

`Wait-Process -Name {{process_name}} -Timeout {{30}}`
