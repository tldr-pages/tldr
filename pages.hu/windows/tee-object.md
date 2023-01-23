# Tee-Object

> A parancs kimenetét egy fájlba vagy változóba menti, és elküldi a csővezetékben. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/tee-object>.

- Folyamatok kiadása egy fájlba és a konzolra:

`Get-Process | Tee-Object -FilePath {{path/to/file}}`

- Folyamatok kimenete egy változóba és a `Select-Object`:

`Get-Process notepad | Tee-Object -Variable {{proc}} | Select-Object processname,handles`
