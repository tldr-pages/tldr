# Set-Acl

> Cambia el descriptor de seguridad de un elemento especificado, como un archivo o una clave de registro.
> Nota: Este comando solo puede usarse a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-acl>.

- Copiar un descriptor de seguridad de un archivo a otro:

`$OriginAcl = Get-Acl -Path {{ruta\al\archivo}}; Set-Acl -Path {{ruta\al\archivo}} -AclObject $OriginAcl`

- Usar el operador pipeline para pasar un descriptor:

`Get-Acl -Path {{ruta\al\archivo}} | Set-Acl -Path {{ruta\al\archivo}}`
