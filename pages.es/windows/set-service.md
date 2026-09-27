# Set-Service

> Inicia, detiene y suspende un servicio, y cambia sus propiedades.
> Nota: Este comando solo puede usarse a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-service>.

- Cambia el nombre para mostrar:

`Set-Service -Name {{hostname}} -DisplayName "{{nombre}}"`

- Cambia el tipo de inicio de servicios:

`Set-Service -Name {{service_name}} -StartupType {{Automatic}}`

- Cambia la descripción de un servicio:

`Set-Service -Name {{service_name}} -Description "{{descripción}}"`
