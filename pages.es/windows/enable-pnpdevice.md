# Enable-PnpDevice

> El cmdlet Enable-PnpDevice habilita un dispositivo Plug and Play (PnP). Debe usar una cuenta de Administrador para habilitar un dispositivo.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/pnpdevice/enable-pnpdevice>.

- Habilitar un dispositivo:

`Enable-PnpDevice -InstanceId 'ID OBTENIDO USANDO EL COMANDO Get-PnpDevice'`

- Habilitar todos los dispositivos PnP deshabilitados:

`Get-PnpDevice | Where-Object {$_.Problem -eq 22} | Enable-PnpDevice`

- Habilitar un dispositivo sin confirmación:

`Enable-PnpDevice -InstanceId 'ID OBTENIDO USANDO EL COMANDO Get-PnpDevice' -Confirm:$False`

- Simulación de lo que sucedería si se ejecuta el cmdlet:

`Enable-PnpDevice -InstanceId 'USB\VID_5986&;PID_0266&;MI_00\7&;1E5D3568&;0&;0000' -WhatIf:$True`
