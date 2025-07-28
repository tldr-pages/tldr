# PSVersionTable

> Una variable de solo lectura (como `$PSVersionTable`) para obtener la versión actual de PowerShell.
> Este comando solo se puede ejecutar en PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables#psversiontable>.

- Imprimir un resumen de la versión y edición de PowerShell actualmente instaladas:

`$PSVersionTable`

- Obtener el número de versión detallado (mayor, menor, compilación y revisión) de PowerShell:

`$PSVersionTable.PSVersion`

- Listar todas las versiones de script de PowerShell compatibles que esta versión de PowerShell admite:

`$PSVersionTable.PSCompatibleVersions`

- Obtener el ID del último commit de Git en el que se basa la versión de PowerShell actualmente instalada (funciona en PowerShell 6.0 y posteriores):

`$PSVersionTable.GitCommitId`

- Verificar si el usuario está ejecutando PowerShell Core (6.0 o posterior) o la "Windows PowerShell" original (versión 5.1 o anterior):

`$PSVersionTable.PSEdition`
