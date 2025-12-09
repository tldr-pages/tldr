# Set-Location

> Muestra el directorio de trabajo actual o va a un directorio diferente.
> Nota: Este comando sólo se puede utilizar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Ir al directorio especificado:

`Set-Location {{ruta\al\directorio}}`

- Ir a un directorio específico en una unidad diferente:

`Set-Location {{C}}:{{ruta\al\directorio}}`

- Ir y muestra la ubicación del directorio especificado:

`Set-Location {{ruta\al\directorio}} -PassThru`

- Subir al directorio padre del directorio actual:

`Set-Location ..`

- Ir al directorio principal del usuario actual:

`Set-Location ~`

- Regresar/ir al directorio elegido anteriormente:

`Set-Location {{-|+}}`

- Ir a la raíz de la unidad actual:

`Set-Location \`
