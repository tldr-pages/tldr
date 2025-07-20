# Remove-AppxPackage

> Utilidad de PowerShell para eliminar un paquete de aplicación de las cuentas de usuario.
> Más información: <https://learn.microsoft.com/powershell/module/appx/Remove-AppxPackage>.

- Eliminar un paquete de aplicación:

`Remove-AppxPackage {{paquete}}`

- Eliminar un paquete de aplicación para un usuario específico:

`Remove-AppxPackage {{paquete}} -User {{nombre_de_usuario}}`

- Eliminar un paquete de aplicación para todos los usuarios:

`Remove-AppxPackage {{paquete}} -AllUsers`

- Eliminar un paquete de aplicación pero preservar sus datos de aplicación:

`Remove-AppxPackage {{paquete}} -PreserveApplicationData`
