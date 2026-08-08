# Start-Service

> Inicia servicios detenidos.
> Nota: Este comando solo puede usarse a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/start-service>.

- Inicia un servicio usando su nombre:

`Start-Service -Name {{nombre_del_servicio}}`

- Muestra información sin iniciar un servicio:

`Start-Service -DisplayName *{{nombre}}* -WhatIf`

- Inicia un servicio deshabilitado:

`Set-Service {{nombre_del_servicio}} -StartupType {{manual}}; Start-Service {{nombre_del_servicio}}`
