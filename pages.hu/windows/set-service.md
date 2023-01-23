# Set-Service

> Egy szolgáltatás indítása, leállítása és felfüggesztése, valamint tulajdonságainak módosítása. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-service>.

- Megjelenítő név módosítása:

`Set-Service -Name {{hostname}} -DisplayName "{{name}}"`

- A szolgáltatások indítási típusának módosítása:

`Set-Service -Name {{service_name}} -StartupType {{Automatic}}`

- Egy szolgáltatás leírásának módosítása:

`Set-Service -Name {{service_name}} -Description "{{description}}"`
