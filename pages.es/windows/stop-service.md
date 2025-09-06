# Stop-Service

> Detiene servicios en ejecución.
> Nota: Este comando solo puede usarse a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/stop-service>.

- Detener un servicio en el equipo local:

`Stop-Service -Name {{nombre_del_servicio}}`

- Detener un servicio usando el nombre para mostrar:

`Stop-Service -DisplayName "{{nombre}}"`

- Detener un servicio que tiene servicios dependientes:

`Stop-Service -Name {{nombre_del_servicio}} -Force -Confirm`
