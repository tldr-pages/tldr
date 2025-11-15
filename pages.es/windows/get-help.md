# Get-Help

> Muestra información de ayuda y documentación para los comandos de PowerShell (alias, cmdlets y funciones).
> Este comando solo se puede ejecutar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-help>.

- Muestra información de ayuda general para un comando específico de PowerShell:

`Get-Help {{comando}}`

- Muestra una documentación más detallada para un comando específico de PowerShell:

`Get-Help {{comando}} -Detailed`

- Muestra la documentación técnica completa para un comando específico de PowerShell:

`Get-Help {{comando}} -Full`

- Imprime solo la documentación para un parámetro específico del comando de PowerShell (usa `*` para mostrar todos los parámetros), si está disponible:

`Get-Help {{comando}} -Parameter {{parámetro}}`

- Imprime solo los ejemplos del cmdlet, si están disponibles:

`Get-Help {{comando}} -Examples`

- Lista todas las páginas de ayuda de cmdlet disponibles:

`Get-Help *`

- Actualiza la base de conocimientos de ayuda y documentación actual usando `Update-Help`:

`Update-Help`

- Ve una versión en línea de la documentación del comando de PowerShell en el navegador web predeterminado:

`Get-Help {{comando}} -Online`
