# Get-Acl

> Obtener el descriptor de seguridad para un recurso, como un archivo o una clave del registro.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>.

- Mostrar la ACL para un directorio específico:

`Get-Acl {{ruta\al\directorio}}`

- Obtener una ACL para una clave del registro:

`Get-Acl -Path {{HKLM:\System\SetDeControlesActual\Control}} | Format-List`
