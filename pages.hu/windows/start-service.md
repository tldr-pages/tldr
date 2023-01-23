# Start-Service

> Egy vagy több leállított szolgáltatás indítása. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/start-service>.

- Indítson el egy szolgáltatást a neve segítségével:

`Start-Service -Name {{service_name}}`

- Információk megjelenítése szolgáltatás indítása nélkül:

`Start-Service -DisplayName *{{name}}* -WhatIf`

- Letiltott szolgáltatás indítása:

`Set-Service {{service_name}} -StartupType {{manual}}; Start-Service {{service_name}}`
