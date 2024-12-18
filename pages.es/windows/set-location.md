# Set-Location

> Muestra el directorio de trabajo actual o va a un directorio diferente.
> Nota: Este comando sólo se puede utilizar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Va al directorio especificado:

`Set-Location {{ruta\al\directorio}}`

- Va a un directorio específico en una unidad diferente:

`Set-Location {{C}}:{{ruta\al\directorio}}`

- Va y muestra la ubicación del directorio especificado:

`Set-Location {{ruta\al\directorio}} -PassThru`

- Sube al padre del directorio actual:

`Set-Location ..`

- Va al directorio principal del usuario actual:

`Set-Location ~`

- Regresa/va al directorio elegido anteriormente:

`Set-Location {{-|+}}`

- Va a la raíz de la unidad actual:

`Set-Location \`
