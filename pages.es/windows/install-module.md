# Install-Module

> Instala módulos de PowerShell desde PowerShell Gallery, NuGet y otros repositorios.
> Más información: <https://learn.microsoft.com/powershell/module/powershellget/install-module>.

- Instala un módulo o lo actualiza a la última versión disponible:

`Install-Module {{módulo}}`

- Instala un módulo con una versión específica:

`Install-Module {{módulo}} -RequiredVersion {{versión}}`

- Instala un módulo no anterior a una versión específica:

`Install-Module {{módulo}} -MinimumVersion {{versión}}`

- Especifica un rango de versiones compatibles (inclusive) del módulo requerido:

`Install-Module {{módulo}} -MinimumVersion {{versión_mínima}} -MaximumVersion {{versión_máxima}}`

- Instala el módulo desde un repositorio específico:

`Install-Module {{módulo}} -Repository {{repositorio}}`

- Instala el módulo desde repositorios específicos:

`Install-Module {{módulo}} -Repository {{repositorio1 , repositorio2 , ...}}`

- Instala el módulo para todos/usuario actual:

`Install-Module {{módulo}} -Scope {{AllUsers|CurrentUser}}`

- Realiza una simulación para determinar qué módulos se instalarán, actualizarán o eliminarán a través de `Install-Module`:

`Install-Module {{módulo}} -WhatIf`
