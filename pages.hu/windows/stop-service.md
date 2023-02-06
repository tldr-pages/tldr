# Stop-Service

> Egy vagy több futó szolgáltatás leállítása. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/stop-service>.

- Egy szolgáltatás leállítása a helyi számítógépen:

`Stop-Service -Name {{service_name}}`

- Egy szolgáltatás leállítása a megjelenített név használatával:

`Stop-Service -DisplayName "{{name}}"`

- Függő szolgáltatásokat tartalmazó szolgáltatás leállítása:

`Stop-Service -Name {{service_name}} -Force -Confirm`
