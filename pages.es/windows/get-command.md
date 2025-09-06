# Get-Command

> Lista y obtiene los comandos disponibles en la sesión actual de PowerShell.
> Este comando solo se puede ejecutar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-command>.

- Lista todos los comandos de PowerShell disponibles (alias, cmdlets, funciones) en el computador actual:

`Get-Command`

- Lista todos los comandos de PowerShell disponibles en la sesión actual:

`Get-Command -ListImported`

- Lista solo los alias/cmdlets/funciones de PowerShell disponibles en el computador:

`Get-Command -Type {{Alias|Cmdlet|Function}}`

- Lista solo programas o comandos disponibles en PATH en la sesión actual:

`Get-Command -Type Application`

- Lista solo comandos de PowerShell por el nombre del módulo, por ejemplo, `Microsoft.PowerShell.Utility` para comandos relacionados con utilidades:

`Get-Command -Module {{módulo}}`

- Obtiene la información del comando (por ejemplo, número de versión o nombre del módulo) por su nombre:

`Get-Command {{comando}}`
